# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkheight(node):
            if not node:
                return 0
            leftH = checkheight(node.left)
            rightH = checkheight(node.right)
            if leftH<0 or rightH<0 or abs(leftH-rightH)>1:
                return -1
            return max(leftH, rightH) +1

        return checkheight(root) != -1