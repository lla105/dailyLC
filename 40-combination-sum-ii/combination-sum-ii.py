class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        c.sort()
        result = []

        def bt(curList, index, current_sum):
            if current_sum == target:
                result.append(list(curList))
                return
            if current_sum > target:
                return
            for i in range(index, len(c)):
                if i>index and c[i] == c[i-1] :
                    continue
                bt( curList+[c[i]] , i+1 , current_sum+c[i] )
        bt( [] , 0, 0)
        return result