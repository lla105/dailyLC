# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxD = 0
        def dfs(node, maxD):
            if node is None:
                # print('.  returning 0')
                return 0
            # print(f'[{node.val}] : going left')
            leftH = dfs(node.left, maxD)
            # print(f'[{node.val}] : going right')
            rightH = dfs(node.right, maxD)
            tempHighest = max(leftH, rightH)
            maxD = max(tempHighest, maxD)
            # print(f'[{node.val}] maxD+1 : f{maxD+1}')
            return maxD + 1
        maxD2 = dfs(root, maxD)
        return maxD2