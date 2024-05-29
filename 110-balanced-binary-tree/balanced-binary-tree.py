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
        def trav(node):
            if node is None:
                return 0
            leftreturn = trav(node.left)
            rightreturn = trav(node.right)
            if abs(leftreturn-rightreturn) > 1:
                return -1
            if leftreturn==-1 or rightreturn==-1:
                return -1
            return max(leftreturn, rightreturn) +1
        temp = trav(root)
        if temp is -1:
            return False
        else:
            return True