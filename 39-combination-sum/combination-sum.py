class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def trav(candindex, remainsum, curlist):
            if remainsum == 0:
                resultlist.append(curlist)
                return
            if remainsum < 0 :
                return
            for i in range(candindex, len(candidates)):
                trav(i , remainsum-candidates[i] , curlist + [candidates[i]])
        resultlist = []
        trav(0, target, [])
        return resultlist