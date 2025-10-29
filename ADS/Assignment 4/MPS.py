
import numpy as np
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
        
        def is_member(self, id):
            bucket = self._hash_(id)
            current = self.hash_table[bucket]

            while current!=None:
                if current.MpsID == id:
                    return True
                else:
                    current = current.next
            return False
        def add_user_to_list(self,mpsID, name, phone, accNo):
            
                

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

        

        
