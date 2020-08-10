// solution3.0
    // speed upper 98%
    // memory upper 10%

class Solution {
    
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        
        // 기존에 소거할 케이스들 리턴 - 길이 0, 1
        guard !( head == nil || head?.next == nil )else{
            return head
        }
        //
        var tail : ListNode?
        var node = head
        var count = 0
        while node != nil {
            tail = node
            node = node!.next
            count += 1
        }
        //
        var k = k % count
        if k == 0 { return head }
        // head 이동 칸 수
        var slice = count - k
        
        //
        var prev : ListNode?
        node = head
        while slice > 0 {
            prev = node
            node = node!.next
            slice -= 1
        }
        
        prev!.next = nil
        tail!.next = head
        return node
        
    }// func
}// class
