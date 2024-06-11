class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {}
        if target not in nums:
            return -1
        for i in range(len(nums)):
            d[nums[i]] = i
        return d[target]