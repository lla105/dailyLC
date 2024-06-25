class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.result = []
        def trav(available, curlist):
            if len(curlist) == len(nums):
                self.result.append(curlist)
                return
            for i in range(len(available)):
                nextcurlist = curlist + [available[i]]
                nextavailable = available[:i] + available[i+1:]
                trav(nextavailable, nextcurlist)

        trav(nums, [])
        return self.result