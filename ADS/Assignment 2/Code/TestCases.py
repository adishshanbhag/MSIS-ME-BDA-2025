from Question_1 import *
LL = singleLinkedList()

def add_head_test():
    LL.add_at_head(10)
    # assert LL.get_count() == 1
    # print("Element added at head")
    # LL.displayLL()

def add_tail_test():
    LL.add_at_tail(20)
    # print("Element added at tail")
    assert LL.get_count() == 2
    # LL.displayLL()

# def delete_head_test():
#     print("Before deleting head")
#     LL.displayLL()
#     result = LL.delete_head()
#     assert LL.get_count() == 1
#     print("\nDeleted element at head: {}".format(result))
#     LL.displayLL()

# def delete_tail_test():
#     print("Before deleting tail")
#     LL.displayLL()
#     result = LL.delete_tail()
#     assert LL.get_count() == 1
#     print("\nDeleted element at tail: {}".format(result))
#     LL.displayLL()

def after_given_data_test():
    LL.add_after_data(10,15)
    LL.add_after_data(15,20)
    LL.add_after_data(20,25)
    # assert LL.get_count() == 4
    # print("All elements added after given data")
    # LL.displayLL()

def delete_after_data_test():
    # print("Before deleting the element")
    # LL.displayLL()
    result = LL.delete_after_data(15)
    # assert LL.get_count() == 3
    # print("\nElement {} deleted after given data".format(result))
    # LL.displayLL()

def search_ele_test():
    element = 20
    assert LL.search_Element(element)
    print("Element {} found in linked list".format(element))
    LL.displayLL()

add_head_test()
after_given_data_test()
search_ele_test()

# delete_after_data_test()
# add_tail_test()
# delete_tail_test()
# delete_head_test()
