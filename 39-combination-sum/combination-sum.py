class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def bt(curList, index):
            if sum(curList) == target:

                result.append(curList)
                return
            if sum(curList) > target:
                return
            
            for i in range(index, len(candidates)):
                bt(curList + [candidates[i]], i)
            
        bt([], 0)

        return result