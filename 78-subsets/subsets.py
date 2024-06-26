class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = set()

        def bt(availableList , curList , startindex) :
            curList = sorted(curList)
            self.result.add( tuple(curList) )

            for i in range(startindex, len(availableList)):
                nextavailableList = availableList[:i] + availableList[i+1:]
                tempA = nextavailableList
                tempB = curList + [availableList[i]]
                # bt(nextavailableList , curList[availableList[i]])
                bt(tempA, tempB, startindex)

        bt(nums, [], 0)
        return self.result