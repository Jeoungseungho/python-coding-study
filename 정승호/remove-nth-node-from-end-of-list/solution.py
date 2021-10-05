# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        s = head
        total = 0
    
        while s:
            total+=1
            s = s.next
    
        position = total - n + 1    

        i = 1
        while i < position-1:
            f = f.next
            i+=1
        if position==1:
            f = f.next
            return f
        else:
            f.next = f.next.next
            return head
