class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go through nums left to right
        length = len(nums)
        right = [1]*length
        left = [1]*length
        for i in range(length):
            if i!=0 :
                left[i] = left[i-1] * nums[i-1]
        print(f'left : {left}')
        # go through nums backwards 
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        print(f'right: {right}')

        # result = []
        result = [1]*length
        for i in range(length):
            result[i] = right[i] * left[i]
        return result


# nums = 1,2,3,4
# [0] = a*2*3*4
# [1] = 1*b*3*4
# [2] = 1*2*c*4
# [3] = 1*2*3*d

# right = [a,b,c,d] = [24, 12, 4, 1]
# left = [a,b,c,d]. = [1 ,  1, 2, 6]






































        # length = len(nums)
        # right = [1] * length
        # left = [1] * length

        # for i in range(1, length, 1):
        #     left[i] = nums[i-1] * left[i-1]

        # for i in range(length-2, -1, -1) :
        #     right[i] = right[i+1] * nums[i+1]
        # answer = []
        # for i in range(length):
        #     answer.append(right[i] * left[i])

        # return answer

