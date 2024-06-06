# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.isbalanced = True

        def trav(node):
            if node is None:
                return 0
            leftH = trav(node.left)
            rightH = trav(node.right)
            print(node.val, leftH, rightH)
            if abs(leftH - rightH) > 1:
                self.isbalanced = False
            temphigher = max(leftH, rightH)

            return temphigher+1

        trav(root)

        return self.isbalanced