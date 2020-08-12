class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.len = 0 # 큐 내부의 자료의 갯수를 구함
        self.max_size = k
        self.queue = [None for _ in range(k)]
        self.front = self.rear = -1
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        # Queue is full
        if self.len == self.max_size:
            return False
        
        # Queue is Empty
        elif self.rear == -1 :
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            self.len += 1
            return True
            
        else : 
            # Next position of rear
            self.rear = (self.rear + 1) % self.max_size 
            self.queue[self.rear] = value
            self.len += 1
            return True
        
        
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        
        # Queue is empty
        if self.len == 0:
            return False
        
        # Only one component
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1

        
        else :
            self.front = (self.front+1) % self.max_size
        self.len -= 1
        return True
        
        
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.len == 0:
            return -1
        else :
            return self.queue[self.front]
        
        
        
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.len == 0:
            return -1
        else :
            return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.len == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
