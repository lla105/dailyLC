# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        self.answer = None
        def traverse(node):
            if not node or node.val==p.val or node.val==q.val:
                return node
            
            left = traverse(node.left)
            right = traverse(node.right)
            if left and right:
                self.answer = node
                return node
            if left:
                return left
            if right:
                return right

        return traverse(root)
        return self.answer