/**
 * Definition for singly-linked list.

 * public class ListNode {

 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }

 * }
 */

class Solution {
    
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        
        // 만약 길이가 0,1 이면 바로 헤드 그대로 리턴
        guard !( head?.next == nil || k == 0 || head == nil ) else{
            return head
        }
        
        // 1. 길이 찾기
        var length = 1
        var now0 = head
        while let next0 = now0?.next {
            length += 1
            now0 = next0
        }
        
        let nth = k % length
        // 회전 시작
        guard !(nth == 0) else {
            return head
        }
        
        // 길이가 2이상인 연결리스트 이다.
        var head = head
        
        for _ in ( 1...(nth) ) {
        
            // 1). 마지막 이전, 마지막 노드를 찾는다.
            var prev : ListNode? = nil
            var current : ListNode? = head
            while let nextNode = current?.next {
                // current의 .next가 nil이 아닐 때 까지 다음을 반복
                prev = current
                current = nextNode
            }
            // prev : 마지막 -1 노드 레퍼런스
            prev?.next = nil
            // current : 마지막 노드 레퍼런스
            current?.next = head
            // 새로운 헤드가 된 current
            head = current
        }
        
       // 마지막으로 헤드에 지정된 노드 옵셔널로 리턴
       return head
    }
}
