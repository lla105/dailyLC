# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findsubroot(node):
            if not node:
                return
            if node.val == subRoot.val:
                print('found root :', node.val)
                self.subrootnodes.append(node)
                # return 
            findsubroot(node.left)
            findsubroot(node.right)

        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                isSameTree(p.left, q.left)
                isSameTree(p.right, q.right)
                return 
            self.issubtree = False
            return False

        self.subrootnodes = []
        findsubroot(root)
        # print(self.subrootnodes)
        for node in self.subrootnodes:
            self.issubtree = True
            print('node : ', node.val)
            isSameTree( node, subRoot)
            if self.issubtree == True:
                return True
        # isSameTree(self.subrootnode ,subRoot)
        if not self.subrootnodes:
            return False
        else:
            return self.issubtree
