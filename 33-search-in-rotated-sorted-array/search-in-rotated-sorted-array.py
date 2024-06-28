class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # d = {}
        # for i in range(len(nums)):
        #     d[nums[i]] = i
        # return d.get(target, -1 )
        if len(nums) == 2:
            for i in range(len(nums)):
                if target==nums[i]:
                    return i
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (l+r) // 2
            print(l,m,r)
            if nums[m]==target:
                return m
            elif nums[l] <= nums[m] :
                # left is sorted
                if nums[l] <= target < nums[m]:
                    # target is on left side.
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                # right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m-1
        return -1