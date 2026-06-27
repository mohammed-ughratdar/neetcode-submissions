class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp1 = head
        temp2 = head.next
        head.next = None

        while(temp2 != None):
            temp = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp
        
        return temp1