class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
    
              
        

if __name__ == "__main__":
    A = LinkedList()
    A.insert_at_beginning(5)
    A.insert_at_end(89)
    A.insert_at_end(90)
    A.insert_at_beginning(76)
    print(A)