# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = []
        def trav(node):
            if not node:
                return node
            self.nums.append(node.val)
            left = trav(node.left)
            right = trav(node.right)
            return
        trav(root)
        # print(self.nums)
        heapq.heapify(self.nums)
        count= 0
        while count < k-1 :
            # print(self.nums)
            heapq.heappop(self.nums)
            count+=1
        # print(self.nums)
        return self.nums[0]