class Solution {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
     
        // 0,1 개면 바로 리턴
        if (head == nil || head?.next == nil){
            return head
        }
        
        // 2개 이상의 노드있다.
        var stack : [Int] = []
        var lastValue  : Int? = nil
        var node = head
        
        // stack 완성시키기
        while node != nil {
            // 첫 입력
            if lastValue == nil {
                stack.append( node!.val )
                lastValue = node!.val
                node = node?.next
                continue
            }else{
                // lastValue와 새로운 노드 값이 다를 경우
                if node!.val != lastValue! {
                    stack.append( node!.val )
                    lastValue = node!.val
                    node = node?.next
                    continue
                }else{
                    // lastValue와 새로운 노드 값이 같았다.
                    if let topValue = stack.last{
                        if topValue == node!.val {
                            // lastValue, topValue와 같을 경우
                            stack.popLast()
                            node = node?.next
                            continue
                        }else{
                            // lastValue와 같으나, topValue와 다들 경우
                            node = node?.next
                            continue
                        }
                    }else{
                        // lastValue와 같으나, 이미 탑 발류가 팝되었고, 스택이 비었을 경우
                        node = node?.next
                        continue
                    }
                }
            }
        }
        
        // 스택이 비어버린 경우
        if stack.isEmpty {
            return nil
        }
        
        // 스택에 한 개 이상 남은 경우
            // 스택
        var head : ListNode? = ListNode( stack.removeFirst() )
        var node1 : ListNode? = head
        for val in stack {
            var newNode : ListNode? = ListNode( stack.removeFirst() )
            node1?.next = newNode
            node1 = node1?.next
        }
        
        return head
    }
}
