class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        c = candidates

        result = []

        def bt(curList, index):
            if sum(curList) > target:
                return
            if sum(curList) == target:
                result.append(curList)

            for i in range(index, len(c)):
                bt(curList + [c[i]] , i)

        bt([] , 0)

        return result