# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # def trav(curpath , available):
        #     if len(curpath) == len(nums) :
        #         result.append(curpath)
        #         return
        #     for i in range(len(available)):
        #         nextpath = curpath + [available[i]]
        #         nextavailable = available[:i] + available[i+1:]
        #         trav(nextpath , nextavailable)
        # trav([] , nums)
        # return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res
            
