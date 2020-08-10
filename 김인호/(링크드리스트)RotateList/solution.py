# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 노드개 한개 또는 없을때 예외처리
        if head == None or head.next == None:
            return head
        temp = head
        length = 1
        # 링크드 리스트의 길이를 구한다.
        while temp.next != None:        
            temp = temp.next
            length += 1
        # 반복 횟수를 줄임.
        k %= length
        if k == 0:
            return head
        for i in range(k):
            temp = head
            # 끝을 빼고 앞에다가 붙임.
            while True:
                if temp.next == None:
                    tail.next = None
                    temp.next = head
                    head = temp
                    break
                tail = temp
                temp = temp.next
        return head