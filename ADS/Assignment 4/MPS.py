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

    class database:
        def __init__(self, capacity):
            self.capacity = capacity
            self.table = [[] for _ in range(self.capacity)]   
        def _hash(self, value):
            return value%self.capacity
        def insert(self, user):
            index = self._hash(user.MpsID)
            if self.table[index] is not None:
                temp = self.table[index]
                while temp.next!=None:
                    temp = temp.next
                temp.next = user
            else:
                

    class userRegistration:
        
        class User:
            def __init__(self, name, phone, accNo):
                self.name = name
                self.phone = phone
                self.accNo = accNo
                self.MpsID = 0
                self.next = None
                self.reg_Check_and_Id_Gen()
                self.debit_Count = {}
                self.money_Debited = {}
                self.transaction_History = []

            def reg_Check_and_Id_Gen(self):
                if (self.name is not None and self.phone != 0 and self.accNo != 0):
                    self.MpsID = self.enrolled_Count + 1
                    self.enrolled_count += 1
                else:
                    print("Registration Failed!!! Details not filled properly. Please try again")
        
        def __init__(self):
            self.head = None
            self.enrolled_Count = 1
            self.tail = None

        def add_user_to_list(self, name, phone, accNo):
            
        