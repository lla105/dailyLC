# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        self.arr = []

        def trav(node):
            if not node:
                return
            self.arr.append(node.val)
            trav(node.left)
            trav(node.right)
            return
        trav(root)
        print(self.arr)
        self.arr = sorted(self.arr)
        
        # return self.arr[k]
        return self.arr[k-1]
