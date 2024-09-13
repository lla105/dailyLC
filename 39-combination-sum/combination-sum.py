class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        if not c :
            return []
        outputList = set()

        def bf( curList ) :
            if sum(curList) > target :
                return
            if sum(curList) == target:
                
                outputList.add( tuple(sorted(curList)) )
                return
            for i in range(len(c)):
                bf( curList+[c[i]])
        bf( [] )
        return outputList
