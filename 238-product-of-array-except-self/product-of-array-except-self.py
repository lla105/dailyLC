class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        result = []
        for i in range(len(nums)):
            right.append(1)
            left.append(1)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        print(left)
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        print(right)
        for i in range(len(nums)):
            result.append(0)
            result[i] = left[i] * right [i]

        return result


# right = [24,12,4,1]
# left. = [1, 1, 2,6]