# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        size = 0
        while current is not None:
            current = current.next
            size += 1
            
        if n == size:
            head = head.next
            return head
        
        i=0
        current = head
        
        while i < size - n -1:
            current = current.next
            i += 1
        
        print(current)
        current.next = current.next.next   
        
        return head
        
        