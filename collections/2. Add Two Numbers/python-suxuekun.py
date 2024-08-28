# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        while l1 and l2:
            l1.val = l2.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            
        h1 = h2 = h1 if l1 else h2
        while h2:
            if h2.val >=10:
                if not h2.next:
                    h2.next = ListNode(1,)
                else:
                    h2.next.val+=1
                h2.val = h2.val %10
            h2 = h2.next
        return h1