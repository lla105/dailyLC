# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output_arr = [] # format : [ [val1], [val2,val3], ... ] 
        d = {} #format : { level:[val1,val2] }
        
        # 3,9,20 > lvl=1 > output_arr=[ [3], [9] ] , len()=2 , [ [3], [9,20] ]
        # 3,9,20,25 > lvl=2 > [ [3], [9,20] ] , len()=2 , [ [3], [9,20], [15] ]


        def trav( node, level ) :
            if not node:
                return
            if level >= len(output_arr) :
                output_arr.append( [node.val] )
            else: 
                output_arr[level].append(node.val)
            # if level in d:
            #     d[level].append(node.val)
            # else:
            #     d[level] = [ node.val ]
            left = trav( node.left, level+1 )
            right = trav( node.right, level+1 )
            return 
        trav( root , 0)

        # for level, val_list in d.items():
        #     output_arr.append( tuple(val_list) )
        return output_arr