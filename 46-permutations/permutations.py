class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outputList = []
        def bf( curList , availableNums ):
            if len(curList) == len(nums):
                print(' appending : ', curList )
                outputList.append( tuple(curList) )
                return
            
            for i in range(len( availableNums )):
                nextcurList = curList + [availableNums[i]]
                nextaNums = availableNums[:i] + availableNums[i+1:]
                bf( nextcurList , nextaNums )

        bf( [] , nums )
        return outputList
# [] [1,2,3] -> 1 -> 2,3
# [1] [2,3] -> 2 -> 3
# [1,2] [3] -> 3 -> [] -> append

# [] [1,2,3] -> 2 -> 1,3
# [2] [1,3] -> 1 -> 3
# [2,1] [3] -> 3 -> []
# [2,1,3]