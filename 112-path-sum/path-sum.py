# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
           
                return False
            
        self.answer = False
        def trav( node, cursum ):
            # if not node : 
            #     # print(' leaf : ', cursum)
            #     if cursum == targetSum:
            #         self.answer = True
            #         return True
            #     return False
            if not node:
                return
            # print('>> ', node.val, '--> ', cursum+node.val)
            if not node.left and not node.right and cursum+node.val==targetSum:
                self.answer = True
                return True
            trav(node.left, cursum+node.val)
            # if left:
            #     return left
            trav(node.right, cursum+node.val)
            # if right:
            #     return right
        trav( root, 0)
        return self.answer
