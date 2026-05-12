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


    def Reverse_Linked_List(self):

        current = self.head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev


if __name__ == "__main__":
    A = Linkedlist()
    A.insert_at_beginning(4)
    A.insert_at_beginning(8)
    A.insert_at_beginning(9)
    A.insert_at_end(12)
    A.Reverse_Linked_List()
    A.Print()