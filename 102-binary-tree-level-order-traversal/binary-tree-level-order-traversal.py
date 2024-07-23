# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        leveld = defaultdict(list)

        def dfs(node, level):
            if not node:
                return node
            leveld[level].append(node.val)
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            return
        dfs(root, 0)
        result = []
        for i,v in leveld.items():
            result.append(v)
        return result
