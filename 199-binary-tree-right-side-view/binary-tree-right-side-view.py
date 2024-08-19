# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.d = {}
        def trav( node , level ) :
            if not node:
                return node
            self.d[level] = node.val
            left = trav(node.left , level + 1) 
            right = trav(node.right, level + 1)


            return node.val
        trav(root, 0)
        # temp = []

        for i,v in self.d.items():
            self.result.append(v)
        return self.result