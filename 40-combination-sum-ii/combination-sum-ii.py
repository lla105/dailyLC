class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        c = sorted(c)
        result = []
        result2 = set()
        def bt(curList , index):
            if sum(curList) > target:
                return
            if sum(curList) == target:
                # result.append(curList[:])
                # curList = sorted(curList)
                # # print(curList)
                result2.add( tuple(sorted(curList)) )
                return
            else:
                for i in range(index , len(c)):
                    if i>index and c[i]==c[i-1]:
                        continue
                    bt( curList + [c[i]] , i+1 )

        bt([] , 0 )
        return result2