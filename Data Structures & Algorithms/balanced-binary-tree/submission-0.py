# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxHeight = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        

        def balanced(root: Optional[TreeNode]):

            if root == None:
                return 0

            left_node = 1+ balanced(root.left)
            right_node = 1+ balanced(root.right)                 
            self.maxHeight = self.maxHeight and abs(left_node - right_node) <= 1

            return max(left_node,right_node)

        balanced(root)
        return self.maxHeight
