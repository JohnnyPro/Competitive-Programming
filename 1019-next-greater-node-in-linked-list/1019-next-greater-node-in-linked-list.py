# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        stack = []
        reverseList = []
        result = []
        
        while current:
            reverseList.append(current.val)
            current = current.next
            
        reverseList.reverse()
        for i in reverseList:
            while stack and stack[-1] <= i:
                stack.pop()
                
            if stack:
                result.append(stack[-1])
            else:
                result.append(0)
                
            stack.append(i)
        
        result.reverse()
        return result 