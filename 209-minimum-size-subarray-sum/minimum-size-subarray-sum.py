class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l = 0
        count = len(nums) + 1
        tempsum = 0
        
        for i in range(len(nums)):
            tempsum += nums[i]
            print('1.1tempsum : ', tempsum)

            while tempsum >=target:
                print('  tempsum>target, count = ', count,'vs',i-l+1)
                count = min(count, i-l+1)
                tempsum -= nums[l]
                l+=1
                print('1.2 tempsum : ', tempsum)

        # arr.pop(0)
        # print(/)
        return count