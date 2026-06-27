# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None

        lnode = self.invertTree(root.left)
        rnode = self.invertTree(root.right)

        root.left = rnode
        root.right = lnode

        return root