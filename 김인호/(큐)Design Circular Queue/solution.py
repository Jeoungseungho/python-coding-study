class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k + 1
        self.rear = 0
        self.front = 0
        self.cq = [-1] * (self.size)

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.cq[self.rear] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.cq[(self.front + 1) % self.size]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.cq[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.rear == self.front:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.rear + 1) % self.size == self.front:
            return True
        return False
