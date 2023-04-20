
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        current = mergedList
        
        while list1 or list2:
            if not list2:
                print('here')
                current.next = list1
                break
           
            if not list1:

                current.next = list2
                break
               
            current.next = ListNode()
            current = current.next
            if list1.val <= list2.val:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next
                
                
        return mergedList.next