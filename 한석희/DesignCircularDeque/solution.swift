class MyCircularQueue {
    
    var readIndex = 0
    var writeIndex = 0
    var ringSize : Int
    var baseArray : Array<Int?> = [ ]

    /** Initialize your data structure here. Set the size of the queue to be k. */
    init(_ k: Int) {
        ringSize = k
        baseArray = Array<Int?>(repeating: nil, count: ringSize)
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    func enQueue(_ value: Int) -> Bool {
        
        guard !isFull() else {return false}
        
        baseArray[ writeIndex % ringSize ] = value
        writeIndex += 1
        
        return true
        
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    func deQueue() -> Bool {
        
        guard !isEmpty() else {
            return false
        }
        
        readIndex += 1
        return true
        
    }
    
    /** Get the front item from the queue. */
    func Front() -> Int {
        
        if isEmpty(){
            return -1
        }
        
        return baseArray[ readIndex % ringSize ]!
    }
    
    /** Get the last item from the queue. */
    func Rear() -> Int {
        
        // no ele
        if isEmpty(){
            return -1
        }
        
        //
        return baseArray[ ( (writeIndex-1) % ringSize ) ]!
    }
    
    /** Checks whether the circular queue is empty or not. */
    func isEmpty() -> Bool {
        
        if writeIndex - readIndex == 0 {
            return true
        }
        
        return false
        
    }
    
    /** Checks whether the circular queue is full or not. */
    func isFull() -> Bool {
        
        if ( (( writeIndex - readIndex ) == ringSize) && (writeIndex != 0) ) {
            return true
        }
        
        return false
    }
    
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * let obj = MyCircularQueue(k)
 * let ret_1: Bool = obj.enQueue(value)
 * let ret_2: Bool = obj.deQueue()
 * let ret_3: Int = obj.Front()
 * let ret_4: Int = obj.Rear()
 * let ret_5: Bool = obj.isEmpty()
 * let ret_6: Bool = obj.isFull()
 */
