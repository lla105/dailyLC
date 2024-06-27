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
        self.d = {} #format : { level:val }
        def trav(level, node):
            if not node:
                print(' empty...')
                return
            print('  ', level, node.val)
            self.d[level] = node.val
            trav(level+1, node.left)
            trav(level+1, node.right)
            return
        trav(0,root)
        print(self.d)
        result = []
        for i,v in self.d.items():
            result.append(v)
        return result