class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if both are None, they are flip equivalent
        if not root1 and not root2:
            return True
        # If one is None and the other is not, they are not flip equivalent
        if not root1 or not root2:
            return False
        # If the values of the roots are different, they are not flip equivalent
        if root1.val != root2.val:
            return False
        
        # Check if the children are flip equivalent in one of two ways:
        # 1. The left children are flip equivalent, and the right children are flip equivalent.
        # 2. The left child of root1 is flip equivalent to the right child of root2 and vice versa.
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
