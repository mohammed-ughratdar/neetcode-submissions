# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.max_val = -200
        self.good_nodes = 0
        def dfs(root: TreeNode, max_val: int):
            if not root:
                return
            
            if root.val >= max_val:
                max_val = root.val
                self.good_nodes += 1

            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, self.max_val)
        return self.good_nodes

        