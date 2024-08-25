class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        num = numbers
        while l<r:
            if num[l]+num[r] > target:
                r -= 1
            elif num[l]+num[r] < target :
                l += 1
            else:
                return (l+1,r+1)

        