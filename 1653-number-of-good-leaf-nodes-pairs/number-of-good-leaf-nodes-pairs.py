# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0
        def bt(node):
            if not node:
                return []
            if not node.left and not node.right: # is leaf
                return [1]
            leftdist = bt(node.left)
            rightdist = bt(node.right)
            if leftdist and rightdist:
                for d1 in leftdist:
                    for d2 in rightdist:
                        if d1+d2 <= distance:
                            self.pairs+=1
            alldist = leftdist + rightdist
            templist = []
            for dist in alldist:
                templist.append(dist+1)
            return templist
        bt(root)

        return self.pairs