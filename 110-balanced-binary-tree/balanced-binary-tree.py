# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def trav(node):
            if node is None:
                return 0
            leftHeight = trav(node.left)
            rightHeight = trav(node.right)
            if abs(leftHeight-rightHeight) > 1:
                return -1
            if leftHeight==-1 or rightHeight==-1:
                return -1
            return max(leftHeight, rightHeight) +1

        temp = trav(root)
        if temp==-1:
            return False
        else:
            return True