# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def trav(leftnode, rightnode):
            if not leftnode and not rightnode:
                return True
            if (leftnode and not rightnode) or (rightnode and not leftnode) or leftnode.val!=rightnode.val:            
                return False
            temp1 = trav(leftnode.left, rightnode.right)
            temp2 = trav(leftnode.right,rightnode.left)
            return temp1 and temp2
        return trav(root, root)
        # return True