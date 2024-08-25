# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def trav( node ):
            if not node:
                return None
            if node==p:
                return node
            if node==q:
                return node
            left = trav(node.left)
            right= trav(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        return trav(root)
