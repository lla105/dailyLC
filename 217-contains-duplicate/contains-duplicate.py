class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tempset = set()
        for n in nums:
            if n in tempset:
                return True
            else:
                tempset.add(n)