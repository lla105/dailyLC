class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target==0:
            return []
        self.results = set()

        #index for candidates.
        # curArray for [2,2,3], or [7]
        def bf(index , curArray):
            if sum(curArray) > target:
                return
            if sum(curArray)==target:
                # curArray = sorted(curArray)
                self.results.add( tuple(curArray) )
                return
            for i in range( index, len(candidates)):
                c = candidates[i]
                nextArray = curArray + [c]
                bf(i,nextArray)
        bf(0, [])
        return self.results