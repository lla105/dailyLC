# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def trav(node):
            if node is None:
                print('   returning 0')
                return 0
            print(f'[{node.val}] : calling left')
            leftH = trav(node.left)
            print(f' [{node.val}] : calling right')
            rightH = trav(node.right)
            print(f'  [{node.val}] : {leftH} vs {rightH}')
            maxD = max(leftH, rightH) +1
            return maxD
        return trav(root)
        # return maxD