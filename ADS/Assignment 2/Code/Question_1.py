class singleLinkedList:
    class _node_:
        def __init__(self, ele):
            self.data = ele
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def get_count(self):
        return self.count
    
    def displayLL(self):
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.head
            while cur!=None:
                print("{} ".format(cur.data), end=" ")
                cur = cur.next

    def displayCircularLL(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        nodes = []
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(nodes)
        
#add head element
    def add_at_head(self, ele):
        new_node = self._node_(ele)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count+=1

#add tail element
    def add_at_tail(self,ele):
        new_node = self._node_(ele)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    
#delete head
    def delete_head(self):
        if not self.is_empty():
            cur = self.head.next
            self.head.next = None
            result = self.head.data
            del(self.head)
            self.head = cur
            self.count-=1
            return result
        return None
    
#delete tail element
    def delete_tail(self):
        if not self.is_empty():
            cur = self.tail
            prev = self.head
            while prev.next!=cur :
                prev= prev.next
            prev.next = None
            result = cur.data
            del(cur)
            self.tail = prev
            self.count = self.count - 1
            return result
        return None
    
#add element after data
    def add_after_data(self,key, ele):
        if not self.is_empty():
            cur = self.head
            while cur.data != key and cur!=None:
                cur = cur.next
            if cur!=None:
                new_node = self._node_(ele)
                new_node.next = cur.next
                cur.next = new_node
                if cur == self.tail:
                    self.tail = new_node
                self.count+=1
        else:
            print("Linked list is empty")
    
#delete element after data
    def delete_after_data(self,key):
        if not self.is_empty():
            cur = self.head
            while cur.data!=key and cur!=None:
                cur = cur.next
            if cur!=None and cur.next!=None:
                temp = cur.next
                if self.tail == temp:
                    self.tail = cur
                cur.next = temp.next
                result = temp.data
                temp.next = None
                del(temp)
                self.count-=1
                return result
            else:
                print("No element to delete")
        return None
    
#search element
    def search_Element(self,key):
        if not self.is_empty():
            temp = self.head
            while temp!=None and temp.data!=key:
                temp = temp.next
            if temp!=None:
                return True
        return False
    
    def reverse_LinkedList(self):
        if not self.is_empty():
            curNode = self.head
            nextNode = curNode
            prevNode = None
            while nextNode!=None:
                nextNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                curNode = nextNode
            self.head, self.tail = self.tail, self.head
            
            
    







