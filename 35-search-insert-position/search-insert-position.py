class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) -1

        # while left <= right:
        #     mid = (right-left) // 2 + left
            
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)