# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leftscore = 0
    rightscore = 0
    isbalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # print(root)
        def search(node):
            if not node:
                return 0
            left = search(node.left)
            right = search(node.right)
            # print(f'{node.val} : {left} - {right}')
            if abs(left - right) > 1:
                self.isbalanced = False
            self.leftscore = left
            self.rightscore = right
            return 1+ max(left, right)

        search(root)
        # print(self.leftscore, self.rightscore, "=", abs(self.leftscore - self.rightscore))
        if self.isbalanced:
            return True
        else:
            return False
        

        