# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.middleAncestor = None
        self.pnode = None
        self.qnode = None

        def dfs( node ):
            if not node:
                return False
            if node.val == p.val:
                print(' found p : ', p.val)
                self.pnode = node
                return True
            if node.val == q.val:
                print(' found q : ', q.val)
                self.qnode = node
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                self.middleAncestor = node
                return False
            if left and not right:
                return True
            if right and not left :
                return True
            if not right and not left:
                return False
        dfs(root)
        if self.middleAncestor:
            return self.middleAncestor
        elif self.pnode:
            return self.pnode
        elif self.qnode:
            return self.qnode
