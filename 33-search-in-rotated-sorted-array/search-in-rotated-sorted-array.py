class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # d = {}
        # if target not in nums:
        #     return -1
        # for i in range(len(nums)):
        #     d[nums[i]] = i
        # return d[target]

        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            if nums[l]<=nums[m]: #left is sorted. right is not
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else : # target is on right side, which is not sorted.
                    l = m + 1
            else: #right is sorted, left is not
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else: # t is on left, which is not sorted
                    r = m - 1
        return -1

