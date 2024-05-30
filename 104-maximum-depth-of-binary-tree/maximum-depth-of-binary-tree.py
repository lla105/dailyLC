# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxD = float('-inf')

        def trav(node,maxD):
            if node is None:
                return 0
            leftH = trav(node.left, maxD)
            rightH = trav(node.right, maxD)
            temp = max(leftH, rightH)
            maxD = max(maxD, temp)
            return maxD+1
        return trav(root, maxD)