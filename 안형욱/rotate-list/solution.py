# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next==None:
            return head
        targetNode = head
        count = 1
        while True:
            if targetNode.next == None:
                targetNode.next=head
                k = k%count
                break
            targetNode = targetNode.next
            count+=1
        for _ in range(count-k):
            head = head.next
        targetNode = head
        for _ in range(count-1):
            targetNode = targetNode.next
        targetNode.next = None
        return head