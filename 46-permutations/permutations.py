class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def trav(curpath , available):
            if len(curpath) == len(nums) or not available:
                result.append(curpath)
                return
            for i in range(len(available)):
                nextpath = curpath + [available[i]]
                nextavailable = available[:i] + available[i+1:]
                trav(nextpath , nextavailable)
        trav([] , nums)
        return result
