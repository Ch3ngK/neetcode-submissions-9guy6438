# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle point using slow and fast pointers 
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None # To disconnect the 2 halves 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merging the two halves 
        first, second = head, prev
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1
            first = tmp1
            second = tmp2
