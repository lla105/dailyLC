# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0
        leafs = set()
        def trav(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = trav(node.left)
            right = trav(node.right)
            # if left and right:
            for d1 in left:
                for d2 in right:
                    if d1+d2 <= distance:
                        self.pairs +=1 
            alldist = left + right
            templist = []
            for d in alldist:
                templist.append(d+1)
            return templist
            
        trav(root)
        # print(leafs)


        return self.pairs

        