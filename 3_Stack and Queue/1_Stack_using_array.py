class Stack:
    def __init__(self):
        self.items = []

    def Push(self, data):
        self.items.append(data)

    def Pop(self):
        if not self.items:
            print("Stack is empty")
            return None
        self.items.pop()

    def Top(self):
        if not self.items:
            print("Stack is empty")
            return None
        print(self.items[-1])

    def Size(self):
        print(len(self.items))
    
    def Display(self):
        if not self.items:
            print("Stack is empty")
        else:
            print("Stack (top → bottom):")
            for item in reversed(self.items):
                print(item)

            
if __name__ == "__main__":
    A = Stack()
    A.Push(5)
    A.Push(7)
    A.Push(23)
    A.Push(78)
    A.Top()
    A.Pop()
    A.Top()
    A.Display()
