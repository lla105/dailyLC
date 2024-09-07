# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # head is linked list
    # root is tree
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.answer = False
        def matchlist( treenode , rootnode):
            # print('    ', treenode.val, ' vs ', rootnode.val)
            if treenode.val == rootnode.val:
                # print(' temp match + 1 ->', rootnode.val )
                if rootnode.next == None:
                    # print(" >>> FULL MATCH!!")
                    self.answer = True
                    return True
                if treenode.left :
                    matchlist( treenode.left , rootnode.next)
                if treenode.right :
                    matchlist( treenode.right , rootnode.next)
            else:
                # print(' no more match @ ', rootnode.val )
                return

        def travtree( node ):
            if not node:
                return 

            if node.val == head.val:
                # print('Init match : ', node.val, ' and ', head.val)
                if matchlist( node, head) :
                    return True
            left = travtree( node.left)
            right = travtree( node.right) 
            if left or right:
                return True
            return 
        travtree( root )
        return self.answer

            