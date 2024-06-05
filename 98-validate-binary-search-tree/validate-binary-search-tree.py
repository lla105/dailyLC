# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        self.isvalid = True

        def trav(node, low, high):
            if node is None:
                return 
            leftval = trav(node.left, low, node.val)
            rightval = trav(node.right, node.val , high)
            # if leftval is None: 
            #     leftval=float('-inf')
            # if rightval is None:    
            #     rightval=float('inf')
            print(leftval , node.val , rightval)
            # if leftval>=node.val or node.val>=rightval:
            if low>=node.val or node.val>=high:
                self.isvalid = False
            return 
        trav(root, float('-inf') , float('inf') )
        return self.isvalid