class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            d[num] = d.get(num, 0 ) + 1
            if d[num] > 1:
                return True
        return False