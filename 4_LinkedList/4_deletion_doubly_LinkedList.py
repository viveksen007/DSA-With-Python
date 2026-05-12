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
    
    def delete_at_Pos(self , n):

        if not self.head :
            return

        temp = self.head
        count = 0

        while temp and count < n :
            temp = temp.next
            count += 1

        if not temp :
            print("position out of range")
            return

        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        
        if temp.next is None:
            temp.prev.next = None
            return
        
        prev_node = temp.prev
        Nxt_node = temp.next

        if prev_node:
            prev_node.next = temp.next
        if Nxt_node:
            Nxt_node.prev = temp.prev




if __name__ == "__main__":
    A = Linkedlist()
    A.Insert_At_beginning(5)
    A.Insert_at_end(8)
    A.Insert_At_beginning(45)
    A.Insert_At_beginning(7)
    A.Insert_at_end(80)
    A.delete_at_Pos(1)
    A.Display_Forward()
    A.Display_backward()
