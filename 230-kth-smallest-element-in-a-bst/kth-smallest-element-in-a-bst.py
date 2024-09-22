# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def trav(node):
            if not node:
                return
            arr.append( node.val )
            left = trav(node.left)
            right = trav(node.right)
            return
        trav(root)
        print(arr)
        # arr = sorted(arr)
        heapq.heapify(arr)
        count = 0
        while count < k:
            removed = heapq.heappop(arr)
            count+=1
        return removed