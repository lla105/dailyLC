class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = Counter(nums)
        print(temp)
        for n,i in temp.items():
            # print(n,i)
            if i!=1:
                return True