# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# intution is to use slow and fast pointer
#  

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = head
        fast = dummy
        prev_tail = dummy

        curr = head

        while curr:

            for i in range(k):
                if fast.next:
                    fast = fast.next
                else:
                    return dummy.next

            nxtbatch = fast.next
            fast.next = None

            current = slow
            prev = None

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            prev_tail.next = prev
            prev_tail = slow
            prev_tail.next = nxtbatch
            slow = nxtbatch
            fast = prev_tail
            curr = slow
        return dummy.next
                






        