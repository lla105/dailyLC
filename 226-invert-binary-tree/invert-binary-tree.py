# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def trav(node):
    if node==None:
        return None
    node.left, node.right = node.right, node.left
    trav(node.left)
    trav(node.right)
    # return 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        trav(root)
        return root