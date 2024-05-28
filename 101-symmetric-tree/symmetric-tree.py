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

            temp1 = not leftnode and rightnode
            temp2 = not rightnode and leftnode
            if temp1 or temp2 :
                print('leaf mismatch')
                return False
            if  leftnode.val!=rightnode.val:
                print('val diff')
                return False
            temp3= trav(leftnode.left, rightnode.right)
            temp4 = trav(leftnode.right, rightnode.left)
            return temp3 and temp4
        return trav(root,root)