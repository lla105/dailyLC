# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.deepest = 0

        def traverse(node, level):
            if not node:
                return 0
            self.deepest = max(self.deepest ,level)
            left = traverse(node.left, level+1)
            right = traverse(node.right, level+1)
            return max(left,right)
        traverse(root, 0)

        return self.deepest+1