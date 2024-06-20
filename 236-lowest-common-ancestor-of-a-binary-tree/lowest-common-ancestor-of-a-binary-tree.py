# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root :
            return root

        def trav(node, q, p):
            if not node or node.val==q.val or node.val==p.val:
                return node
            left = trav(node.left, q, p)
            right = trav(node.right, q,p)
            if not left:
                return right
            elif not right:
                return left
            else:
                return node
        return trav(root,q,p)