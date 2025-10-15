from Question_1 import *
from LL_Operations import *

LL = LinkedListOperations()

def add_elements():
    LL.add_at_tail(20)
    LL.add_at_tail(40)
    LL.add_at_tail(60)
    LL.add_at_tail(80)
    LL.add_at_tail(90)
    LL.add_at_tail(100)
    LL.add_at_tail(80)


add_elements()
if LL.contains_Cycle():
    print("Linked List contains cycle")
else:
    print("Linked list does not contain cycle")



# LL.makeCircularLL()
# print("Elements before deleting: ")
# LL.displayCircularLL()
# LL.delete_odd_elements()
# print("Elements after deleting: ")
# LL.displayCircularLL()

# LL.middleElement()
# def is_palindrome(LL):
#     result = LL.is_palindrome()
#     if result:
#         print("Is palindrome")
#     else:
#         print("Not a palindrome")
# print("Linked list: ")
# LL.displayLL()
# is_palindrome(LL)
# LL.add_at_head(50)
# print("Updated Linked list: ")
# LL.displayLL()

# is_palindrome(LL)




# LL.reverse_LinkedList()
# assert LL.sum_n_last_elements(3) == 120
# print("Reversed Linked List: ")
# LL.displayLL()
# n = int(input("Enter the number of elements for which sum is required: "))
# sum = LL.sum_n_last_elements(n)
# assert sum == 300
# print("Sum of last {} elements is: {}".format(n,sum))

