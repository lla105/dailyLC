# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        d = {}
        def trav(node, level):
            if not node:
                return
            d[level] = d.get(level, 0)
            d[level] += node.val
            left = trav(node.left, level+1)
            right = trav(node.right, level+1)

        trav(root, 0)
        for i,v in d.items():
            arr.append( -1*v )
        heapq.heapify(arr)
        count = 0
        print(' arr : ', arr)
        while count < k:
            if len(arr)==0:
                return -1
            removed = heapq.heappop(arr)
            count+=1
        
        return removed*-1