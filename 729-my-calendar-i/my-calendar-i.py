class TreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    
    def __init__(self):
        self.root = None
    
    # Helper function to insert an event in the BST
    def _insert(self, node: TreeNode, start: int, end: int) -> bool:
        if start >= node.end:  # New event is after the current event
            if node.right is None:
                node.right = TreeNode(start, end)
                return True
            return self._insert(node.right, start, end)
        elif end <= node.start:  # New event is before the current event
            if node.left is None:
                node.left = TreeNode(start, end)
                return True
            return self._insert(node.left, start, end)
        else:
            # Overlap case
            return False
    
    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            # If the tree is empty, insert the first event
            self.root = TreeNode(start, end)
            return True
        return self._insert(self.root, start, end)

# Example usage
# obj = MyCalendar()
# param_1 = obj.book(start, end)
