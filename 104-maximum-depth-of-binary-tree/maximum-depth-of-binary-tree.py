# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.deepest = 0

        def dfs(node, level):
            if not node:
                return 0
            self.deepest = max(self.deepest, level)
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            return 

        dfs(root, 0)
        return self.deepest+1