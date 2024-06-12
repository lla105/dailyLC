class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.resultlist = []
        s = set()
        def trav(cursum, curlist):
            if cursum == target:
                # self.resultlist.append(curlist)
                curlist.sort()
                s.add( tuple(curlist) )
                return
            if cursum > target:
                return
            for i in range(len(candidates)):
                trav(cursum+candidates[i] , curlist+[candidates[i]])
            return
        trav(0,[])
        for each in s:
            # print(each)
            self.resultlist.append(each)
        return self.resultlist
