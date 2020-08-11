'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def delete_node(self,curr):
        pass

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # list만들어서 해당하는 index 새로운 list node만듬
        prev = None
        curr = head

        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = curr
                curr = curr.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                curr = curr.next
                if prev:
                    prev.next = curr
                else:
                    head= curr

        return head

    def print_linked_list(self,head):
        curr = head
        while curr !=None:
            print(curr.val)
            curr = curr.next

    def insert(self,data_list):
        pass

# a = ListNode(1)
# b = ListNode(2)
# c =ListNode(2)
# d = ListNode(2)
# e = ListNode(3)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
#
# sol = Solution()
#
# sol_list = sol.deleteDuplicates(a)
# sol.print_linked_list(sol_list)
