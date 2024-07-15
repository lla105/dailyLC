# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        child = set()
        nodes = {}
        for p,c,isleft in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if isleft==1:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            # print(nodes[p])
            child.add(c)
            
        # delete all node except root
        for i in range(len(descriptions)):
            d = descriptions[i][0]
            if d not in child:
                return nodes[d]
        rootnode = None

        # for i,v in nodedic.items():
        #     if i==rootval:
        #         rootnode = v
        # print('root node: \n', rootnode)
        return rootnode
                
