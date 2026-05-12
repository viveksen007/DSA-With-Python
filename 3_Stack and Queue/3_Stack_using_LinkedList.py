class StackNode:

    def __init__(self , data , next = None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def Push(self , data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def Pop (self):
        if not self.top:
            print("Stack is Empty")
            return
        popped = self.top.data
        self.top = self.top.next
    
    def Top(self):
        if not self.top:
            print("Stack is Empty")
            return
        print(self.top.data)

    def Size(self):

        count = 0
        temp = self.top

        while temp:
            temp = temp.next
            count += 1

        print(count)

    def Display(self):

        temp = self.top
        print("Stack Top -> Bottom")
        while temp:
            print(temp.data)
            temp = temp.next
    
if __name__ == "__main__":
    A = Stack()
    A.Push(5)
    A.Push(9)
    A.Push(2)
    A.Push(7)
    A.Pop()
    A.Top()
    A.Display()
