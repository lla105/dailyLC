class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            z = nums[i]
            if z==0:
                zeros+=1
            if z==1:
                ones+=1
            if z==2:
                twos+=1
        result = []
        print(zeros,ones,twos)
        print(result)
        for i in range(zeros):
            result.append(0)
        print(result)

        for i in range(ones):
            result.append(1)
        print(result)

        for i in range(twos):
            result.append(2)
        print(result)
        for i in range(len(nums)):
            nums[i] = result[i]
        return result