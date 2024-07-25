# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True

        def traverse(node, upper, lower):
            if not node:
                return None
            if lower>=node.val or node.val>=upper:
                self.isbalanced = False
            left = traverse(node.left, node.val, lower)
            right = traverse(node.right, upper, node.val)
            return

        traverse(root, float('inf') , float('-inf'))
        return self.isbalanced