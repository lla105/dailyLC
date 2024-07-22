# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, curList):
            if not node:
                return None
            if not node.left and not node.right:
                result.append( curList + [str(node.val)] )
            left = dfs(node.left, curList + [str(node.val)]+ ['->'] )
            right = dfs(node.right, curList +[ str(node.val)]+ ['->'] )
            return node.val
        dfs(root, [])
        for i in range(len(result)):
            arr = result[i]
            result[i] = ''.join(arr)
        return result