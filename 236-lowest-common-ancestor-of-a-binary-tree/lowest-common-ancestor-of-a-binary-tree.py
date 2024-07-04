# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def bt(node):
            if not node:
                return None
            if node.val==p.val or node.val==q.val:
                return node
            
            left = bt(node.left)
            right = bt(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right

        return bt(root)