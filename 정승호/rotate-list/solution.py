# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # LinledList is Empty
        if not head :
            return head
        
        temp = head
        length = 1 # store length of LinkedList
        while (temp.next != None):
            temp = temp.next
            length += 1
            
            
        # k is bigger than length of LinkedList    
        if k > length:
            k = k % length
        
        # Change k to right rotation 
        k = length - k
        
        # No rotation needed
        if k == 0 or k == length:
            return head
        
        current = head
        cnt = 1
        
        while (cnt < k) and current.next != None: 
            current = current.next
            cnt +=1
            
        if current == None:
            return head
        
        kNode = current 
        temp.next = head
        head = kNode.next
        kNode.next = None
        
        return head
        
        
