class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        c = sorted(c)
        output = []
        def bf( curList , index ) :
            if sum(curList) == target:
                output.append( tuple(curList) )
                return
            if sum(curList) > target:
                return

            for i in range( index , len(c)):
                if i>index and c[i]==c[i-1]:
                    continue
                bf( curList+[c[i]] , i+1)
        bf( [] , 0 )
        return output