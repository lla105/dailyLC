class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.resultlist = set()
        c = candidates
        def bt( curList, alist , index) :
            if sum(curList) > target:
                return
            if sum(curList) == target:
                # self.resultlist.append( tuple(curList) )
                self.resultlist.add( tuple(sorted(curList)) )
                # self.resultlist.add( tuple(curList))
                return

            # print(curList, alist)
            for i in range( index, len(alist)):
                nextcurList = curList+[alist[i]]
                # nextalist = alist[:i] + alist[i+1:]
                if i>index and c[i]==c[i-1]:
                    continue
                bt( nextcurList , alist , i+1)
        bt( [] , c , 0)

        return self.resultlist