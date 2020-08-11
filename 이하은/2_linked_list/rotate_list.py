'''
https://leetcode.com/problems/rotate-list/
'''

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:

    def changeList(self,head):

        curr = head
        prev = None
        while curr.next != None:
            prev = curr
            curr = curr.next

        new_head = curr
        new_head.next = head
        prev.next = None

        return new_head

    def read(self,head):
        curr = head
        while curr != None:
            print(curr.val)
            curr = curr.next

    def rotateRight(self,head:ListNode,k:int)->ListNode:

        for _ in range(k):
            head = self.changeList(head)
        # self.read(head)
        return head

#
# a = ListNode(1)
# b = ListNode(2)
# c =ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
#
# sol = Solution()
# sol.rotateRight(a,2)
