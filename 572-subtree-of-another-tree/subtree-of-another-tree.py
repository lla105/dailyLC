# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def findsubroot(node):
            if not node:
                return None
            if node.val == subRoot.val:
                self.samenodes.append(node)
            left = findsubroot(node.left)
            right = findsubroot(node.right)
            if left: return left
            if right: return right
            return None
        
        def issubtree(node,subRoot):
            if not node and not subRoot:
                return True
            if (node and not subRoot) or (subRoot and not node):
                return False
            if node.val == subRoot.val:
                return issubtree(node.left , subRoot.left) and issubtree(node.right, subRoot.right)
            else:
                return False
        self.samenodes = []
        rootnode = findsubroot(root)
        print(rootnode)
        for startnode in self.samenodes:
            if issubtree(startnode, subRoot):
                return True
        return False

        return root