# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        def bt(node, low, high):
            if not node:
                return 
            
            bt(node.left, low, node.val)
            bt(node.right, node.val, high)
            if low < node.val < high:
                pass
            else:
                self.answer = False
                return


        bt(root,float('-inf') , float('inf'))
        return self.answer