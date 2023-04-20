# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        tempHead = None
        cmltr = [] 
        while True:
            if len(cmltr) == k:
                finalPointer = cmltr[-1].next
                if tempHead:
                    tempHead.next = cmltr[-1]
                else:
                    head = cmltr[-1]
                while len(cmltr) > 1:
                    popped = cmltr.pop()
                    popped.next = cmltr[-1]
                
                lastOne = cmltr.pop()
                lastOne.next = finalPointer
                tempHead = lastOne
                
            if current == None:
                break
            cmltr.append(current)    
            current = current.next
            
        return head 