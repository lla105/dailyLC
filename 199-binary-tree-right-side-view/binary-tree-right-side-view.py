# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.d = {} # format : { level1:val1, level2:val2, ...}
        def trav( node , level ) :
            self.d[level] = node.val
            if node.left:
                trav(node.left, level+1)
            if node.right:
                trav(node.right, level+1)

        trav( root, 0 )
        # print(self.d)
        result = []
        for i,v in self.d.items():
            result.append(v)
        return result