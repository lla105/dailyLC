# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.isBalanced = True
        def bt(node, low, high):
            if not node:
                return None
            
            bt(node.left, low, node.val)
            bt(node.right, node.val , high)

            print(low , node.val, high, end=' ----> ')
            if low < node.val and node.val < high:
                print('good')
                pass
            else:
                print('BAD')
                self.isBalanced = False
            return node.val
            

        bt(root, float('-inf') , float('inf'))
        return self.isBalanced