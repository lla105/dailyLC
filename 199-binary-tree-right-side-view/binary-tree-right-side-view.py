# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {} # format : { level1:val1, level2:val2, ...}
        def trav( node , level ) :
            if not node:
                return 
            self.d[level] = node.val
            trav(node.left, level+1)
            trav(node.right, level+1)

        trav( root, 0 )
        # print(self.d)
        result = []
        for i,v in self.d.items():
            result.append(v)
        return result