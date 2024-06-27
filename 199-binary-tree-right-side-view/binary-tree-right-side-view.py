# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {} # format { level:node.val }
        def trav(level, node):
            if not node:
                return 
            # print('>>>', level, node.val)
            self.d[level] = node.val
            left = trav(level+1, node.left)
            right = trav(level+1, node.right)
        trav(0, root)

        result = []
        for i,v in self.d.items():
            result.append(v)
        return result