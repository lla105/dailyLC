class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur = 0
        prev = 0

        for money in nums:
            print(f'max({money}+{prev} , {cur})')
            temp = cur
            cur = max(money+prev,cur)
            prev = temp

        return cur
