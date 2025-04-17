class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] :
                    remainder = ( i * j ) %k
                    if remainder == 0 :
                        output += 1

        return output