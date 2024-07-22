# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def backtrack(node):
            if not node:
                return 0
            left = backtrack(node.left)
            right = backtrack(node.right)
            self.longest = max(self.longest, left+right)
            longerpath = max(left, right)
            return longerpath + 1
        backtrack(root)
        return self.longest