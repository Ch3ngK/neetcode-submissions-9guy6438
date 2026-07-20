# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2): # Alternate between sorted lists in "lists"
                l1 = lists[i]

                if (i + 1) < len(lists): 
                    l2 = lists[i + 1] 
                else: 
                    l2 = None
                mergedLists.append(self.mergeLists(l1, l2))
            
            lists = mergedLists
        return lists[0]


    def mergeLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        list1curr = list1
        list2curr = list2
        
        if list1 is None: 
            return list2

        if list2 is None: 
            return list1    

        while (list1curr and list2curr):
            if (list1curr.val <= list2curr.val):
                tail.next = list1curr
                list1curr = list1curr.next
            else:
                tail.next = list2curr
                list2curr = list2curr.next
            tail = tail.next

        if not list1curr:
            tail.next = list2curr
        else: 
            tail.next = list1curr

        return dummy.next