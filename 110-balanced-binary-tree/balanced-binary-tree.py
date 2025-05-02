# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def trav( node ) :
            if not node:
                return 0

            left = trav(node.left)
            right = trav(node.right)
            if abs(left-right) > 1:
                self.result = False
            if left > right:
                return left+1
            else:
                return right+1
        trav( root)
        return self.result