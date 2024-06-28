class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {}
        for i in range(len(nums)):
            # d[i] = nums[i]
            d[nums[i]] = i
        print(d)
        return d.get(target, -1 )
        return -1