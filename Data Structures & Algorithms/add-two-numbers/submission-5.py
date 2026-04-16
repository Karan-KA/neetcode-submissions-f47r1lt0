# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = ListNode(0)
        head = curr
        nextnode = None
        quotient = 0
        while l1 or l2 or quotient:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumval = val1 + val2 + quotient
            remainder = sumval % 10
            quotient  = sumval // 10
            node = ListNode(remainder)
            curr.next = node
            curr = node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next



