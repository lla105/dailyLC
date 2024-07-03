# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.isBalanced = True
        def trav(node):
            if not node:
                return 0
            
            leftH = trav(node.left)
            rightH = trav(node.right)

            HeightDiff = abs(leftH-rightH)
            if HeightDiff > 1:
                self.isBalanced = False
            return max(leftH , rightH) + 1

        trav(root)
        return self.isBalanced