class Queue:

    def __init__(self):
        self.items = []

    def Enqueue(self , data):
        self.items.append(data)

    def Dequeue(self):
        if not self.items:
            print("queue is empty")
            return
        self.items.pop(0)

    def Front(self):
        if not self.items:
            print("Queue is Empty")
            return
        print(self.items[-1])
    
    def Size(self):
        print(len(self.items))

    def Display(self):
        if not self.items:
            print("Queue is empty")
        else:
            print("Queue (front → rear):")
            for item in self.items:
                print(item)


if __name__ == "__main__":
    A = Queue()
    A.Enqueue(5)
    A.Enqueue(7)
    A.Enqueue(23)
    A.Enqueue(78)
    A.Front()
    A.Dequeue()
    A.Front()
    A.Display()