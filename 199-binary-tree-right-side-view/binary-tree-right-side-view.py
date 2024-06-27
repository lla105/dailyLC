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
        self.d = {}
        def trav(level, node):
            if not node:
                return
            
            trav(level+1, node.left)
            trav(level+1, node.right)
            # print('   ', level, node.val)
            self.d[level] = node.val
        trav(0, root)
        print(self.d)
        result = []
        # for i,v in self.d.items():
        #     result.append(v)
        i = 0
        while i in self.d:
            result.append(self.d[i])
            i+=1
        return result