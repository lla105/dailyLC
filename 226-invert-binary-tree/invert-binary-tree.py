# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rev( node ):
            if not node:
                return None
            if node.left and node.right:
                node.left , node.right = node.right , node.left
            elif node.left :
                node.right = node.left
                node.left = None
            elif node.right :
                node.left = node.right
                node.right = None
            else:
                return
            rev(node.left)
            rev(node.right)
        rev(root)
        return root