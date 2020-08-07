// 첫 풀이
    // 정확성 : 통과
    // 효율성 : 시간 초과

class Solution {
    
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        
        if k == 0 {
            return head
        }
        // 만약 길이가 0,1 이면 바로 헤드 그대로 리턴
        guard !( head == nil || head?.next == nil ) else{
            return head
        }
        
        // 길이가 2이상인 연결리스트 이다.
        var head = head
        
        // 회전 시작
        for _ in (1...k) {
            // 1). 마지막 이전, 마지막 노드를 찾는다.
            var prev : ListNode? = nil
            var current : ListNode? = head
            // 2).
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
