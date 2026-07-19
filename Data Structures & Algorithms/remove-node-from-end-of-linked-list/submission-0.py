# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        arr = []
        curr = head

        while curr: 
            arr.append(curr.val)
            curr = curr.next

        length = len(arr)
        arr.pop(length - n)
        for val in arr:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next

        