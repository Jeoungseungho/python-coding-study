class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.Q = [-1] * k
        self.size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # Q: full
        if self.isFull():
            return False

        # Q: empty
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.Q[self.rear] = value
            return True

        else:
            self.rear = (self.rear + 1) % self.size
            self.Q[self.rear] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        #Q : empty
        if self.isEmpty():
            return False

        #Q : one element left
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
            return True
        else:
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.front == -1:
            return -1
        else:
            return self.Q[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.rear == -1:
            return -1
        else:
            return self.Q[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.rear == self.front == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        # if all(x!= -1 for x in self.Q):
        #     return True
        length = abs(self.rear-self.front) + 1
        if length == self.size:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()