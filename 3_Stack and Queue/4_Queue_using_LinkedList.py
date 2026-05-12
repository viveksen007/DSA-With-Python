class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def Enqueue(self, data):
        new_node = QueueNode(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def Dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        dequeued = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        print(f"popped -> {dequeued}")

    def Front(self):
        if not self.front:
            print("Queue is empty")
            return None
        print(self.front.data)

    def Size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        print(count)

    def Display(self):
        temp = self.front
        print("Queue (front → rear):")
        while temp:
            print(temp.data)
            temp = temp.next
        
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
