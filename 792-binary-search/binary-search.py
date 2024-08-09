class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (l+r) // 2
            cur = nums[m]
            if cur == target:
                return m
            elif cur> target:
                r = m-1
            else:
                l = m+1
        return -1