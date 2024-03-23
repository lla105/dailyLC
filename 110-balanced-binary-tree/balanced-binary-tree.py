class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Check balance condition at each node
            if abs(left_height - right_height) > 1:
                return float('-inf')  # Return a sentinel value if unbalanced
            
            return max(left_height, right_height) + 1
        
        return dfs(root) != float('-inf')
