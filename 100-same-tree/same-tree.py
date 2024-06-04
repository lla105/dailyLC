# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        def trav(p,q):
                if p is None and q is None:
                    return
                if p is None and q:
                    self.isSame = False
                    return 
                if q is None and p:
                    self.isSame = False
                    return
                if q.val != p.val:
                    self.isSame = False
                    return
                print(' calling left from ', p.val, q.val)
                trav(p.left, q.left)
                print(' calling right from ', p.val, q.val)
                trav(p.right, q.right)

                return
        trav(p,q)
        return self.isSame