class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        mostoccur = 0
        mostint = 0
        for i in range(len(nums)):
            num = nums[i]
            d[num] = d.get(num, 0) + 1
            if d.get(num) > mostoccur:
                mostoccur = d.get(num)
                mostint = num

        return mostint