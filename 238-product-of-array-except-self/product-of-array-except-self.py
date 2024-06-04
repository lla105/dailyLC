class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,       2,         3,       4,5]
        # nums = [num2~5,  num1+num3*5, num1*2 * num4*5]
        # left = product of all #s left of cur num
        # right = product of all #s right of cur num

        # nums = [1,2,3,4]
        # right = [24,12,4,1]
        # left = [1,1,2,6]
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        print(left)

        right = [1] * len(nums)
        for i in range(len(nums)-2, -1 , -1):
            right[i] = right[i+1] * nums[i+1]
        print(right)
        resultlist = []
        for i in range(len(nums)):
            temp = right[i] * left[i]
            resultlist.append(temp)
        print(nums)

        return resultlist
