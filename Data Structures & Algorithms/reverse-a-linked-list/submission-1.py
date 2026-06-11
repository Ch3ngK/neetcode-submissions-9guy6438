# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        prev, curr = None, head
        
        while curr != None:
            nextVal = curr.next 
            curr.next = prev
            prev = curr
            curr = nextVal
        
        return prev
