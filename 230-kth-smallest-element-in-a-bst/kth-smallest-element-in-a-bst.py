# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.array = []

        def trav(node):
            if not node: 
                return 
            self.array.append(node.val)
            trav(node.left)
            trav(node.right)
            return
        trav(root)
        temp = sorted(self.array)
        print(temp)
        return temp[k-1]