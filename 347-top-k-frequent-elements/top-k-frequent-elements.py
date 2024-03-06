class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = Counter(nums)
        print(dic)

        dic2 = {}
        for i in range(len(nums) + 1):
            # print(i)
            dic2[i] = []

        print(dic2)

        for v,i in dic.items():
            # print(v,i)
            dic2[i].append(v)
        print("dic2: ", dic2)

        res = []

        for i in range(len(dic2)-1, 0, -1):
            for n in dic2[i]:
                res.append(n)
                if len(res)==k:
                    return res

            
        