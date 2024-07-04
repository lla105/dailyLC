# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(current):
            if not current:
                return None
            if current == p or current == q:
                return current

            left = dfs(current.left)
            right = dfs(current.right)

            if left and right:
                return current

            if left:
                return left
            else:
                return right
    
        return dfs(root)