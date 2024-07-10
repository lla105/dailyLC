class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def bt(curList, available):
            if len(curList)==len(nums):
                result.append(curList)
                return
            
            for i in range(len(available)):
                nextavailable = available[:i]+available[i+1:]
                bt(curList+[available[i]] , nextavailable)
        bt([] , nums)

        return result