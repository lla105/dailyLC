class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = candidates
        t = target
        if not cand:
            return []

        self.result = set()

        def trav(curList, index):
            if target==sum(curList):
                curList = sorted(curList)
                self.result.add( tuple(curList) )
                return
            if target<sum(curList):
                return
                
            for i in range( len(cand)):
                c = cand[i]
                trav( curList+[c] ,0)

        trav([] , 0)

        return self.result
            