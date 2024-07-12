# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def reverse(node):
            if not node:
                return None
            leftnode = reverse(node.left)
            rightnode = reverse(node.right)
            node.left = rightnode
            node.right = leftnode

            return node
        reverse(root)

        return root