class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 노드개 한개 또는 없을때 예외처리
        if head is None or head.next is None:
            return head
        temp = head
        isRemove = False
        # 노드 앞에서 부터 끝까지 순차 탐색
        while temp.next != None:
            # 중복 숫자가 나올시,
            if temp.val == temp.next.val:
                isRemove = True
            # 앞 숫자와 다른 숫자가 나올시,
            else:
                # 삭제할 숫자가 있을시,
                if isRemove:
                    isRemove = False
                    # 중복된 숫자들 다음 노드를 가리킴
                    try:
                        cur.next = temp.next
                    # 리스트 처음부터 중복숫자가 나올경우, 헤드를 중복숫자 다음으로 가리킴
                    except:
                        head = temp.next
                else:
                    # 삭제 할 노드가 없을시, 현재 노드를 커서가 가리킴
                    cur = temp
            temp = temp.next
        # 리스트의 끝이 중복이면 따로 처리.
        if isRemove:
            try: 
                cur.next = temp.next
            except:
                head = temp.next
                
        return head