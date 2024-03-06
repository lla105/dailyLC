class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsset = set(nums)
        longest=  0
        counter = 0

        for n in numsset:
            if n-1 not in numsset:
                counter = 0
                start = n
                temp = []

                while start in numsset:
                    temp.append(start)
                    print(start)
                    start+=1
                    counter+=1
                print(temp)
                longest = max(counter, longest)
        return longest


