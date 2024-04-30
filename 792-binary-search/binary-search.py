class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = ((right-left)//2)+left
            print(left, mid, right)

            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1