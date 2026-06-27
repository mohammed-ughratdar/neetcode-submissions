# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        if not head or not head.next:
            return
        slow_ptr = fast_ptr = head

        while  fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        second = slow_ptr.next
        slow_ptr.next = None

        prev = None
        curr = second

        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first_node = head
        second_node = prev

        while(second_node != None):
            temp_1 = first_node.next
            temp_2 = second_node.next

            first_node.next = second_node
            second_node.next = temp_1
            first_node = temp_1
            second_node = temp_2
         


