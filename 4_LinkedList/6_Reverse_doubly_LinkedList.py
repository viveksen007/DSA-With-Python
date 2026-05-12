class DNode:

    def __init__(self , data , next=None , prev=None):
        self.data = data
        self.next = next
        self.prev = prev
 
class Linkedlist:

    def __init__(self , head = None):
        self.head = head 

    def Insert_At_beginning(self , data):

        new_node = DNode(data , self.head , None)
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def Insert_at_end(self , data):

        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current 

    def insert_at_position(self , data , n):

        new_node = DNode(data)

        if n == 0:
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return 
        

        temp = self.head
        count = 0 

        while temp and count < n :
            temp = temp.next
            count += 1
        
        if count != n :
            print("position out of range")
            return
        
        if temp is None:

            tail = self.head
            while tail.next :
                tail = tail.next
            tail.next = new_node
            new_node.prev = tail
            return

        prev_node = temp.prev    
        new_node.next = temp
        new_node.prev = prev_node
        temp.prev = new_node
        
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node
    
    def Display_Forward (self):
        current = self.head 
        while current:
            print(current.data , end=" <-> ")
            current = current.next
        print("None")
        

    def Display_backward(self):
        temp = self.head

        if not temp :
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data , end=" <-> ")
            temp = temp.prev
        print("None")
    
    def reverse(self):
        temp = self.head
        prev_node = None

        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            prev_node = temp
            temp = temp.prev  

        if prev_node:
            self.head = prev_node


if __name__ == "__main__":
    A = Linkedlist()
    A.Insert_At_beginning(5)
    A.Insert_at_end(8)
    A.Insert_At_beginning(45)
    A.Insert_At_beginning(7)
    A.Insert_at_end(80)
    A.insert_at_position(56 , 3)
    A.reverse()
    A.Display_Forward()
    A.Display_backward()
