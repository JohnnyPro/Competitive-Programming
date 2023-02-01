# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        current = head
        if head is None: return ListNode()
        while current.next != None:
            current = current.next
            count += 1
            
        middleIndex = floor(count/2)
        current = head
        for i in range(middleIndex): current = current.next
        return current