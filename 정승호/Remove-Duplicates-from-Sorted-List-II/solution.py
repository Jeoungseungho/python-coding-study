# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        temp=pre = ListNode(0,None)
        temp.next = curr
        
        while curr and curr.next :
            if curr.val == curr.next.val:
                while (curr and curr.next and curr.val == curr.next.val):
                    curr = curr.next
                
                curr = curr.next
                pre.next = curr
            else : 
                pre = pre.next
                curr = curr.next
                
        return temp.next
