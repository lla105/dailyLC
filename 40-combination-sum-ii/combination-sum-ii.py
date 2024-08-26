class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = set()

        def bf( curList , index ) :
            if sum(curList) == target:
                pendingList = sorted(curList)
                if tuple(pendingList) not in self.result:
                    self.result.add( tuple(pendingList) )
                    return
            if sum(curList) > target:
                return
            for i in range( index, len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                bf( curList + [candidates[i]] , i+1 )
        bf([] , 0) 
        return self.result