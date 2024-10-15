# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of the sorted list
        dummy = ListNode(0)
        current = head  # Pointer to iterate through the original list
        
        while current:
            # At each iteration, we need to insert `current` into the sorted part
            prev = dummy  # Pointer for the sorted list
            # Find the right place to insert `current`
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert `current` into the sorted part
            next_temp = current.next  # Keep track of the next node in the original list
            current.next = prev.next  # Insert current node after prev
            prev.next = current  # Link prev to current
            
            current = next_temp  # Move to the next node in the original list
        
        return dummy.next  # Return the head of the sorted list
