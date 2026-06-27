# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    global_max = 0

    def find_diameter(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_search =  self.find_diameter(root.left)
       
        right_search =  self.find_diameter(root.right)
        self.global_max = max(self.global_max, left_search+right_search)
        return 1+ max(left_search, right_search)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_diameter(root)
        return self.global_max
        