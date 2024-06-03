# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        q = deque()
        q.append(root)
        resultlist = []
        while q:
            curlevel = []
            for i in range(len(q)):
                curnode = q.popleft()
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
                curlevel.append(curnode.val)
            resultlist.append(curlevel)
        return resultlist