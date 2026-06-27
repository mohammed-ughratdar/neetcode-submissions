# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        res = list()
        for l in level_list:
            res.append(l[-1])

        return res
