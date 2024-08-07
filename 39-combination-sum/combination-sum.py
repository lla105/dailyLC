class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resultlist = []
        c = candidates
        def dfs( curList , index ):
            if sum(curList)>target:
                return
            if sum(curList)==target:
                resultlist.append( tuple(curList) )
                return
            for i in range(index, len(c) ):
                dfs( curList+[c[i]] , i)
        dfs([], 0)
        return resultlist