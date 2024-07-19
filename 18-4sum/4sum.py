class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        # print('INPUT: ', nums)
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1
                while l<r:
                    num1 = nums[i]
                    num2 = nums[j]
                    num3 = nums[l]
                    num4 = nums[r]
                    cursum = num1+num2+num3+num4
                    # print('>> ', [num1,num2,num3,num4], '=', cursum)
                    if cursum > target:
                        # print('  cursum > target')
                        r-=1
                    elif cursum < target:
                        # print('  cursum < target')
                        l+=1
                    else:
                        # print('  append : ', (num1,num2,num3,num4) )
                        result.add( (num1,num2,num3,num4) )
                        l+=1
                        r-=1
        return result