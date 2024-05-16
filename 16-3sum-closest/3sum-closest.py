class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindiff = float('inf') #diff closest to target
        nums = sorted(nums)
        minsum = float('inf')
        for i in range(len(nums)):
            num1 = nums[i]
            l = i+1
            r = len(nums) - 1
            while l<r:
                num2 = nums[l]
                num3 = nums[r]
                tempsum = num1+num2+num3
                # print('  ',tempsum,'=',num1,'+',num2,'+',num3)
                if target==tempsum:
                    # print('returning tempsum')
                    return tempsum
                else:
                    if abs(target-tempsum)<mindiff:
                        mindiff = abs(target-tempsum)
                        minsum = tempsum
                if tempsum>target:
                    r-=1
                elif tempsum<target:
                    l+=1
        print('returning mindiff')
        return minsum