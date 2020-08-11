
func divide(list: LinkedList<Int>, by value: Int) {
    
    var xNode = Node(value: value)
    var newHead : Node<Int>? = xNode
    var newTail : Node<Int>? = xNode
    
    //
    var node = list.head
    
    while let nowNode = node {
        
        if nowNode.value > value {
            
            newTail?.next = Node(value: nowNode.value)
            newTail = newTail?.next
            
        }
        else if nowNode.value < value {
            
            let newNode = Node(value: nowNode.value)
            newNode.next = newHead
            newHead = nowNode
            
        }
        else {
            let newNode = Node(value: value, next: nowNode.next)
            nowNode.next = newNode
        } //
        
        node = node?.next
    }

}
