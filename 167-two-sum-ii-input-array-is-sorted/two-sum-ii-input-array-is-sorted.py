class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            leftnum = numbers[l]
            rightnum = numbers[r]
            if leftnum+rightnum > target:
                r -= 1
            elif leftnum+rightnum < target:
                l+=1
            else:
                return [l+1,r+1]