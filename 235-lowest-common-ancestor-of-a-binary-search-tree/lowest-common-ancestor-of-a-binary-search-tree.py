# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        self.answer = None
        def trav(node):
            if node is None:
                return None
            if node.val>p.val and node.val>q.val:
                trav(node.left)
            elif node.val<p.val and node.val<q.val:
                trav(node.right)
            else:
                self.answer = node
                return
        trav(root)
        return self.answer