# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        def trav(root):
            if root is None:
                return None
            leftnode = trav(root.left)
            rightnode = trav(root.right)
            root.left = rightnode
            root.right = leftnode
            return root
        trav(root)
        return root