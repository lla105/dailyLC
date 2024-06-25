class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.result = []

        def bt(availableNums , curList):
            if len(curList) == len(nums):
                self.result.append(curList)
                return
            for i in range(len(availableNums)):
                nextAvailableNums = availableNums[0:i] + availableNums[i+1:]
                nextList = curList + [availableNums[i]]
                bt(nextAvailableNums, nextList)

        bt(nums, [])
        return self.result