class Node:

    def __init__(self , data , next=None):
        self.data = data
        self.next = next 

class Linkedlist:

    def __init__(self , head = None):
        self.head = head

    def insert_at_beginning(self , data):
        new_node = Node(data , self.head)
        self.head = new_node

    def insert_at_end (self , data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        current = self.head 

        while current.next :
            current = current.next

        current.next = new_node 
    
    def Print(self):
        if self.head is None:
            print("linked list is empty")
            return 
        
        current = self.head
        LLstr = ''

        while current:
            LLstr += str(current.data) + " --> "
            current = current.next 

        print(LLstr)

    def Delete_Node(self , data ):
        
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return
        
        prev = None

        while temp and temp.data != data:
            prev = temp
            temp = temp.next


        if temp is None:
            return 
        
        prev.next = temp.next
        temp = None

    def Delete_Node_atPosition(self , n):

        temp = self.head

        if n == 0:
            self.head = temp.next
            temp = None
            return 
        
        prev = None
        count = 0 

        while temp is not None and count < n :
            prev = temp
            temp = temp.next 
            count += 1

        if temp == None:
            print("position out of Range")
            return
        
        prev.next = temp.next
        temp = None


    
if __name__ == "__main__":
    A = Linkedlist()
    A.insert_at_beginning(4)
    A.insert_at_beginning(8)
    A.insert_at_end(9)
    A.insert_at_end(12)
    A.Delete_Node(12)
    A.Print()
