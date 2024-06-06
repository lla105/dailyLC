class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        print(d)
        if target in d:
            return d[target]
        else:
            return -1
        # return 99