class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = len(nums)+1
        curSum, l = 0,0
        for r, n in enumerate(nums):
            curSum += n
            while curSum >= target:
                res = min(res, r-l+1)
                curSum -= nums[l]
                l += 1
        return res % (len(nums)+1)