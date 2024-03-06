class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if len(nums) == 1:
        #     return 
        # nums = [11,11,11,22,22,33,33]
        dic1 = Counter(nums)
        print("dic1: ",dic1)

        freqdic = {}
        for i in range( 0, len(nums)+1, 1):
            # print(i)
            freqdic[i] = []
        print("freq: ", freqdic)

        for v,i in dic1.items():
            if i in freqdic:
                freqdic[i].append(v)
        print("2freq: ", freqdic)

        answer = []
        for i in range(len(freqdic)-1, 0, -1) :
            for jj in freqdic[i]:
                answer.append(jj)
                if len(answer) == k:
                    return answer