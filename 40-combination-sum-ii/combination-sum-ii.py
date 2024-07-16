class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        self.result = set()
        def bt(curList, startindex):

            if sum(curList)>target:
                return
            if sum(curList)==target:
                self.result.add( tuple(curList) )
                return
            else:
                for i in range(startindex, len(c)):
                    if i>startindex and c[i] == c[i-1]:
                        continue
                    bt(curList+[c[i]] , i+1)
        bt([] , 0)
        return self.result