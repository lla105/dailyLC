class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
            if nums[i] == 1:
                ones+=1 
            if nums[i] == 2:
                twos += 1
        index = 0
        for i in range(len(nums)):
            if zeros>0:
                nums[i]= 0
                zeros-=1
            elif ones>0:
                nums[i]=1
                ones-=1
            elif twos>0:
                nums[i]=2
                twos-=1