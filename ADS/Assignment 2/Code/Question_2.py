from Question_1 import *

class common_Elements(singleLinkedList):
    def __init__(self):
        super().__init__()
    
    def find_Common_Ele(self, list1, list2):
        ite = list1.head
        while ite!=None:
            if list2.search_Element(ite.data):
                self.add_at_tail(ite.data)
            ite = ite.next
        if not self.is_empty():
            print("Common Elements added:")
            self.displayLL()
                