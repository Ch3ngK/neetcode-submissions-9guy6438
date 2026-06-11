# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # (O(n) approach + extra overhead) 
        arr = []
        curr = head
        while (curr != None):
            arr.append(curr.val)
            curr = curr.next

        arr.reverse()
        rl = ListNode(0)
        curr = rl

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return rl.next