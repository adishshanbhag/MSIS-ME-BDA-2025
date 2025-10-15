from Question_1 import *
from Question_2 import *

L1 = singleLinkedList()
L2 = singleLinkedList()
CommonList = common_Elements()

L1.add_at_tail(10)
L1.add_at_tail(20)
L1.add_at_tail(30)
L1.add_at_tail(40)

L2.add_at_tail(50)
L2.add_at_tail(30)
L2.add_at_tail(90)
L2.add_at_tail(20)
L2.add_at_tail(10)

CommonList.find_Common_Ele(L1,L2)
# print(CommonList.get_count)
assert CommonList.get_count() == 3
