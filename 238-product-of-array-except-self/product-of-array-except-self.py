class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = [1] * length
        right = [1] * length

        for i in range(1, length, 1):
            left[i] = nums[i-1] * left[i-1]

        for i in range(length-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        answer = [1] * length
        for i in range(0, length,1):
            print(i)
            answer[i] = left[i] * right[i]

        return answer