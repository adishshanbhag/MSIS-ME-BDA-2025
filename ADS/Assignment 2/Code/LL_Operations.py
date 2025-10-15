from Question_1 import *

class LinkedListOperations(singleLinkedList):
    def __init__(self):
        super().__init__()

    def contains_Cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def makeCircularLL(self):
        self.tail.next = self.head
    
    def delete_odd_elements(self):
        if not self.head:
            return
        NodeCount = self.get_count()
        if NodeCount == 1:
            self.head = None
            return
        curNode = self.head
        prevNode = None
        pos = 1
        new_head = self.head.next if self.head.next != self.head else None
        for _ in range(NodeCount):
            nextNode = curNode.next
            if pos % 2 != 0:
                if prevNode:
                    prevNode.next = nextNode
            else:
                prevNode = curNode
            curNode = nextNode
            pos += 1

        self.head = new_head

        if prevNode:
            prevNode.next = self.head
        else:
            self.head = None

    def middleElement(self):
        Elements_to_Search = self.get_count()
        curNode = self.head
        if Elements_to_Search %2 == 0:
            Elements_to_Search/=2
        else:
            Elements_to_Search = int((Elements_to_Search/2)+1)
        while Elements_to_Search>1:
            curNode = curNode.next
            Elements_to_Search-=1
        print("Element in the middle is {}".format(curNode.data))

    def remove_Duplicates(self):
         values = {}
         curnode = self.head
         prevNode = None
         while curnode!=None:
            if curnode.data not in values:
                values[curnode.data] = 1
                prevNode = curnode
            else:
                prevNode.next = curnode.next
                prevNode = curnode
                curnode = curnode.next
                prevNode.next = None
                del prevNode
                continue
            prevNode = curnode
            curnode = curnode.next

    def is_palindrome(self):
        if not self.is_empty():
            rev_list = singleLinkedList()
            curNode = self.head
            #creating a copy of the original linked list
            while curNode!=None:
                rev_list.add_at_tail(curNode.data)
                curNode = curNode.next
            rev_list.reverse_LinkedList()
            curNode=self.head
            curNode_2 = rev_list.head
            list_size = int(self.get_count())
            nodeCount = list_size/2 if list_size%2 == 0 else (list_size/2)+1
            while nodeCount!=0:
                if curNode.data == curNode_2.data:
                    curNode = curNode.next
                    curNode_2 = curNode_2.next
                    nodeCount-=1
                else:
                    break
            return nodeCount == 0
        

    def split_LinkedList(self):
        if not self.is_empty():
            # self.reverse_LinkedList()
            L1 = singleLinkedList()
            L2 = singleLinkedList()
            curNode = self.head
            NodeCount=0
            while curNode!=None:
                if NodeCount%2 == 0:
                    L1.add_at_tail(curNode.data)
                else:
                    L2.add_at_tail(curNode.data)
                curNode = curNode.next
                NodeCount+=1
            print("After splitting:")
            print("First Linked list: ")
            L1.displayLL()
            print("\nSecond Linked List: ")
            L2.displayLL()
    # def reverse_LinkedList(self):
    #     if not self.is_empty():
    #         curNode = self.head
    #         nextNode = curNode
    #         prevNode = None
    #         while nextNode!=None:
    #             nextNode = curNode.next
    #             curNode.next = prevNode
    #             prevNode = curNode
    #             curNode = nextNode
    #         self.head, self.tail = self.tail, self.head
    
    def sum_n_last_elements(self,n):
        if self.is_empty():
            print("No elements to delete")
        elif n<=0:
            print("n value cannot be less than 1")
        else:
            sum_start_ind =self.get_count()-n
            curNode = self.head
            node_count = 0
            sum = 0
            while curNode!=None:
                if node_count >= sum_start_ind:
                    sum+=curNode.data
                node_count+=1
                curNode = curNode.next
            return sum
        
    

            