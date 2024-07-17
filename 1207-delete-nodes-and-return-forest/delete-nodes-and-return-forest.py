# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        todelete = set(to_delete)
        result = set( [root] )
        print(result)
        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in todelete:
                res = None
                result.discard(node)
                if node.left: result.add(node.left)
                if node.right: result.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return res
        dfs(root)

        return result
            
