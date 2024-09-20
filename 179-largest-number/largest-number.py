class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # print(i,j)
                if int(nums[i]+nums[j]) > int(nums[j]+nums[i]) :
                    continue
                else:
                    nums[i], nums[j] = nums[j] , nums[i]
        print(nums)
        result = ''.join(nums)
        if result[0] == '0':
            return '0'
        return result