# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next

        steps = count - n
        dummy = ListNode(0, head)
        prev = dummy

        while steps:
            prev = prev.next
            steps -= 1

        prev.next = prev.next.next

        return dummy.next