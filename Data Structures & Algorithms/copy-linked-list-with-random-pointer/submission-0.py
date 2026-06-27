"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node_map = dict()

        def dfs(node):
            if not node:
                return None

            if node in node_map:
                return node_map[node]
            
            copy = Node(node.val)
            node_map[node] = copy

            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            
            return copy

        return dfs(head)


