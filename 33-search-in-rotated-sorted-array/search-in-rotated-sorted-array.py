class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min_number = min(nums)
        # newarray = []
        # for i in range(len(nums)):
        #     if nums[i] == min_number:
        #         newarray = nums[i:] + nums[:i]
        # print(newarray)

        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left + (right-left)//2 
            print(nums[mid])
            if nums[mid]==target:
                return mid
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1