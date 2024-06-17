class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for num in nums:
            if num==2:
                twos+=1
            if num == 1:
                ones += 1
            if num == 0:
                zeros += 1

        n = len(nums)
        for i in range(n):
            if zeros>0:
                zeros-=1
                nums[i] = 0
            elif ones>0:
                ones-=1
                nums[i] = 1
            elif twos>0:
                twos-=1
                nums[i] = 2
        
            