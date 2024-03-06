class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        right = [1] * length
        left = [1] * length

        for i in range(1, length, 1):
            left[i] = nums[i-1] * left[i-1]
        print(left)

        for i in range(length-2, -1, -1) :
            # print(i)
            right[i] = right[i+1] * nums[i+1]
        print(right)
        answer = []
        for i in range(length):
            answer.append(right[i] * left[i])

        return answer

