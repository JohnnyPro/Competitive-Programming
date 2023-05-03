# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        full = head
        middle = head
        
        while full is not None and full.next is not None:
            full = full.next.next
            middle = middle.next
            
        return middle