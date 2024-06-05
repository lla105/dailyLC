# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isvalid = True
        def trav(node,low, high):
            if node is None:
                return True
            if low>=node.val or node.val>=high:
                self.isvalid = False
                return False
            lefttree = trav(node.left , low, node.val)
            righttree = trav(node.right , node.val, high)

            return 
        trav(root, float('-inf') , float('inf'))
        return self.isvalid