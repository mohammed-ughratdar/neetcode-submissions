class ListNode:
    def __init__(self, key=-1):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.set_list = [ListNode() for _ in range(100)]
        
    def hash(self, key):
        return key%len(self.set_list)

    def add(self, key: int) -> None:
        curr = self.set_list[self.hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        
        curr.next = ListNode(key)


    def contains(self, key: int) -> bool:
        curr = self.set_list[self.hash(key)].next

        while curr:
            if curr.key == key:
                return True
            curr = curr.next

        return False
        

    def remove(self, key: int) -> None:
        curr = self.set_list[self.hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)