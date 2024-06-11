# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        self.answer = TreeNode()
        def trav(node,p,q):
            if not node: 
                return node
            print()
            if node.val>p.val and node.val>q.val:
                trav(node.left,p,q)
            elif node.val<p.val and node.val<q.val:
                trav(node.right,p,q)
            else:
                self.answer = node
                return node
        trav(root,p,q)
        return self.answer
        # return 