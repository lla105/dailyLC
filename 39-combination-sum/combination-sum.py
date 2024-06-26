class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # self.result = []
        self.result = set()
        def backtrack(index, curList):
            if sum(curList) > target:
                return 

            if sum(curList) == target:
                curList = sorted(curList)
                self.result.add( tuple(curList) )
                return
            
            for i in range(index, len(candidates)):
                nextList = curList + [candidates[i]]
                backtrack(i, nextList)
                
        backtrack(0, [])

        return self.result