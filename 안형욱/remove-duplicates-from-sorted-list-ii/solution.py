# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        targetNode = head
        temp = pre = ListNode()
        temp.next = targetNode

        while targetNode and targetNode.next:
            if targetNode.val == targetNode.next.val:
                while targetNode and targetNode.next and targetNode.val == targetNode.next.val:
                    targetNode = targetNode.next
                targetNode = targetNode.next
                pre.next = targetNode
            else:
                pre = pre.next
                targetNode = targetNode.next

        return temp.next