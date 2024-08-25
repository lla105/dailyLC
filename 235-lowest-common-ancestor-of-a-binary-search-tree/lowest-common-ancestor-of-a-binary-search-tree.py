# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.foundleft = None
        # self.foundright = None
        self.answer = None
        def trav(node):
            if not node:
                return None
            if node==p:
                return node
            if node==q:
                return node
            left = trav(node.left)
            right= trav(node.right)
            if left and right:
                self.answer = node
                return node
            if left:
                return left
            if right:
                return right
        return trav(root)
        return self.answer