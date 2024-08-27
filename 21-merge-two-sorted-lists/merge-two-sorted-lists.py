# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # This pointer will be used to build the new list
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the current pointer forward
            current = current.next
        
        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list, which starts from the next of dummy node
        return dummy.next
        