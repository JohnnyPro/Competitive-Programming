# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        previous = head
        current = head.next
        head.next = None
        while current is not None:
            # next = next
            # current's next = previous
            # go to next
            next = current.next
            current.next = previous
            previous = current
        
            current = next
            
        return previous