class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        qsum = 0
        splits = 0
        stacksum = nums[0]
        for i in range(1,len(nums)):
            qsum += nums[i]
        if stacksum >= qsum:
            splits += 1
        for i in range( 1 , len(nums)-1 ):
            rm_num = nums[i]
            qsum -= rm_num
            stacksum += rm_num
            if stacksum >= qsum:
                splits += 1
        return splits
