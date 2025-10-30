from Exceptions import *
import numpy as np
import datetime
import getpass
class MPS:
    #user registration - name, phone no. account no. -- generate MPS ID once done
    #5 debit transaction allowed per day - amount 20k -- if 20 k reached then 3 transactions with daily limit message
    # 10 transaction visibility to users
    # admin to get user count and details

    #additional ideas
    #balance check
    #money transfer within mps users
    #money crediting logic and transaction
    #password for debit
    #hiding the password while typing
    def __init__(self):
        self.enrolled_count = 0
        self.dailyLimit = 0
        self.is_admin = False
    
    class database:
        def __init__(self):
            self.table_size = 11
            self.hash_table = [None]*self.table_size
            self.p = 13
            self.a = np.random.randint(1, self.p-1)
            self.b = np.random.randint(0, self.p-1)

        def _hash_function_(self, id):
            code = 0
            id = str(id)
            for ch in id:
                code = code << 5
                code = code + ord(ch)
            return code
        def _compression_(self, code):
            return ((((code*self.a)+self.b)%self.p)%self.table_size)
        
        def _hash_(self, id):
            code = self._hash_function_(id)
            bucket = self._compression_(code)
            return bucket
        
        def is_member(self, id, return_user = False):
            bucket = self._hash_(id)
            current = self.hash_table[bucket]

            while current!=None:
                if current.MpsID == id:
                    if not return_user: return True 
                    else: return current
                else:
                    current = current.next
            return False
        def add_user_to_Db(self, user):
             if not self.is_member(user.MpsID):
                  bucket = self._hash_(user.MpsID)
                  user.next = self.hash_table[bucket]
                  self.hash_table[bucket] = user
        
        def debit_From_Account(self, mps, user, date, amount):
             if not self.is_member(user.MpsID):
                bucket = self._hash_(user.MpsID)
                current = self.hash_table[bucket]
                while current!=None:
                     if current.MpsID == user.MpsID:
                        break
                     current = current.next
                if user.debit_Count.get(date) is None:
                    user.debit_Count[date] = 1
                    user.money_Debited[date] = amount
                else:
                    if user.debit_Count[date] == mps.dailyLimit:
                        raise DailyTransactionCountExceeded("You have reached your daily debit transaction limit of 5 transactions. Please Try again tomorrow.")
                    elif (user.money_Debited[date] + amount) >= 20000 :
                        self.mps.dailyLimit = 3
                        raise DailyTransactionAmountExceeded ("Your total transaction amount has exceeded 20000. You are now allowed 3 transactions for the day.")
                    
                user.debit_Count[date] += 1
                user.money_Debited[date] += amount
                user.transaction_History.append("{} : {} debited".format(date, amount)) 
        def _show_transaction_history_(self,mps, user, id = 0):
                if not self.mps.is_admin:
                    print("You can view the only the past 10 transactions. For further details, please reach out to the bank admin at admin@mps.in")
                    count = 0
                    len_list = len(user.transaction_History)
                    if len_list < 10 :
                        print(user.transaction_History)
                    else:
                        for item in user.transaction_History[len_list-1:len_list-11:-1]:
                            print(user.transaction_History[item])       

    class userRegistration:
        def __init__(self,mps_instance, name, phone, accNo, passwd):
                self.mps = mps_instance
                self.name = name
                self.phone = phone
                self.accNo = accNo
                self.MpsID = 0
                self.next = None
                self.password = passwd
                self.regis_Check_and_Id_Gen()
                self.debit_Count = {}
                self.money_Debited = {}
                self.transaction_History = []
                

        def regis_Check_and_Id_Gen(self):
                if (self.name is not None and self.phone is not None and self.accNo is not None):
                    self.MpsID = self.mps.enrolled_count
                    self.mps.enrolled_count += 1
                    self.add_user_to_db()
                    print("Registration completed successfully and user added to the database")
                else:
                    print("Registration Failed!!! Details not filled properly. Please try again")
        def add_user_to_db(self):
             database = MPS.database()
             database.add_user_to_Db(self)    
mps = MPS()
db = mps.database()
user = None
while 1:
    print("Welcome to Manipal Payment Systems")
    print("1. New User Registration")
    print("2. Already a User")
    print("3. Admin Login")
    print("3. Exit")
    choice = int(input("Please enter an option: ").strip())
    while 1:
        if choice == 1:
            print("Enter the following details to register on MPS: ")
            name = input("Enter your full name as per Aadhar Card: ")
            phone = input("Enter your 10 digit phone no.: ")
            accNo = input("Enter your bank account number: ")
            passwd = getpass.getpass("Enter the password: ")
            passwdchk = None
            passwdchk = getpass.getpass("Re-enter your password: ")
            if passwdchk!=passwd:
                passwdchk = getpass.getpass("Re-enter your password: ")
            else:
                print("Password mismatch!!!")
            

            user = mps.userRegistration(mps, name, phone, accNo, passwd)
            print("Your mps ID is ", user.MpsID)
            if input("Do you want to continue with a transaction? Y/N").lower() == 'y': 
                choice = 2
            else:
                exit
        if choice == 2:
            id = int(input("Enter your mps ID: "))
            user = db.is_member(id,return_user=True)

        if choice == 3:


        if choice == 4:
            exit  



# user = mps.userRegistration(mps, "Adish Shanbhag", "8722683731", "1122121")

    try:
        db.debit_From_Account(mps, user, datetime.datetime.now() ,5000)

    except DailyTransactionCountExceeded as e:
        print("Warning: ", e)
    except DailyTransactionAmountExceeded as e:
        print("Warning: ", e)
