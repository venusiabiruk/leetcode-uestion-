# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the values from the current nodes or 0 if nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of values and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for next position
            new_digit = total % 10  # Get the last digit of the total
            
            # Create a new node with the new_digit and attach to the result list
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move to the next nodes in the input lists, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next
        