# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maxDiameter = 0
        def trav(node):
            if node is None:
                return 0
            leftD = trav(node.left)
            rightD = trav(node.right)
            self.maxDiameter = max(leftD + rightD , self.maxDiameter)
            return max(leftD , rightD)+1

        trav(root)
        return self.maxDiameter