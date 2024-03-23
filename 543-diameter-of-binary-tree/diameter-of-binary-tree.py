

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            nonlocal answer
            l = dfs(node.left)
            r = dfs(node.right)
            answer = max(answer, l+r)
            return max(l,r)+1

        answer = 0
        dfs(root)
        return answer