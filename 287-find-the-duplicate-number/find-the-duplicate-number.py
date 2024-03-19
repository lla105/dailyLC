class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # print(nums)
        s = set()
        for num in nums:
            # print(num, s)
            if num in s:
                return num
            else:
                s.add(num)

        return 0