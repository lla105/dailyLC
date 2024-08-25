# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def trav( node ) :
            if not node:
                return 0
            left = trav(node.left)
            right = trav(node.right)
            self.longest = max(self.longest, left+right)
            if left > right:
                return left+1
            else:
                return right +1
        trav(root)

        return self.longest