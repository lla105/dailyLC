# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isvalid = True

        def trav(node, low=float('-inf'), high=float('inf')):
            if node is None:
                return True
            
            # Check the current node's value is within the valid range
            if node.val <= low or node.val >= high:
                self.isvalid = False
                return False
            
            # Traverse the left and right subtrees with updated constraints
            left_valid = trav(node.left, low, node.val)
            right_valid = trav(node.right, node.val, high)

            # Return True only if both subtrees are valid
            return left_valid and right_valid
        
        trav(root)
        return self.isvalid