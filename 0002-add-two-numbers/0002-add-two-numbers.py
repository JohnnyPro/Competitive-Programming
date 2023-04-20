# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sumList = ListNode()
        current = sumList
        while l1 != None or l2 != None:
            if l1 == None:
                while l2 != None:
                    current.next = ListNode()
                    current = current.next
                    sumOfNumbers = l2.val + carry
                    carry = sumOfNumbers // 10
                    current.val = sumOfNumbers - carry*10
                    
                    l2 = l2.next
            elif l2 == None:
                while l1 != None:
                    current.next = ListNode()
                    current = current.next
                    sumOfNumbers = l1.val + carry
                    carry = sumOfNumbers // 10
                    current.val = sumOfNumbers - carry*10
                    
                    l1 = l1.next
            else:
                current.next = ListNode()
                current = current.next
                sumOfNumbers = l1.val + l2.val + carry
                carry = sumOfNumbers // 10
                current.val = sumOfNumbers - carry*10
                
                l1 = l1.next
                l2 = l2.next
        
        if carry != 0:
            current.next = ListNode(carry)
            
        return sumList.next