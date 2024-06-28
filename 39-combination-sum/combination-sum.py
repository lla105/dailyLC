class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.result = set()
        def bt(index, curList):

            if sum(curList)==target:
                # print(curList)
                # curList = sorted(curList)
                self.result.add( tuple(curList) )
                return

            if sum(curList) > target:
                return
            
            for i in range(index, len(candidates)):
                bt(i, curList+[candidates[i]])

        bt(0, [])
        return self.result

