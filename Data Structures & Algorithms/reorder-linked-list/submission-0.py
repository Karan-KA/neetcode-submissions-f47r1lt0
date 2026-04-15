# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        next_link_head = slow.next
        prev = None
        current = next_link_head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow.next = None

        next_link_head = prev
        firsthalf = head
        secondhalf = next_link_head
        while secondhalf:
            next1 = firsthalf.next
            next2 = secondhalf.next
            firsthalf.next = secondhalf
            secondhalf.next = next1
            firsthalf = next1
            secondhalf = next2
            

        