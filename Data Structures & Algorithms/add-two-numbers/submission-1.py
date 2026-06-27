# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_node = ListNode(0, None)
        new_list = ListNode(0, None)
        ptr = new_list

        while l1 or l2:
            if l1 and l2:
                nodes_sum = l1.val + l2.val + carry_node.val
                carry_node.val = nodes_sum//10
                nodes_sum = nodes_sum%10
                new_node = ListNode(nodes_sum)
                l1 = l1.next
                l2 = l2.next

            elif l1:
                nodes_sum = l1.val + carry_node.val
                carry_node.val = nodes_sum//10
                nodes_sum = nodes_sum%10
                new_node = ListNode(nodes_sum)
                l1 = l1.next

            elif l2:
                nodes_sum = l2.val + carry_node.val
                carry_node.val = nodes_sum//10
                nodes_sum = nodes_sum%10
                new_node = ListNode(nodes_sum)
                l2 = l2.next

            ptr.next = new_node 
            ptr = new_node
        
        if carry_node.val:
            ptr.next = carry_node

        return new_list.next
        