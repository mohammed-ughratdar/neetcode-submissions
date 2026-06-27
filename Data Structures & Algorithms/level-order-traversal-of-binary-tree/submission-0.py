# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_list = []

        def dfs(level, node):
            if not node:
                return

            if len(level_list)>level:
                level_list[level].append(node.val)
            else:
                level_list.append([node.val])
            level +=1
            dfs(level, node.left)
            dfs(level, node.right)

        dfs(0, root)

        return level_list
