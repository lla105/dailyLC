"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.result = []
        def trav( node ) :
            if not node:
                return
            for child in node.children:
                trav(child)
            self.result.append(node.val)
        trav(root)
        # for each in root.children:
            # print(each.val)
        return self.result