class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        if not c :
            return []
        outputList = set()

        def bf( curList , index ) :
            if sum(curList) > target :
                return
            if sum(curList) == target:
                outputList.add( tuple(curList) )
                return
            for i in range(index, len(c)):
                bf( curList+[c[i]] , i )
        bf( [], 0)
        return outputList
