class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==1:
            return [1]

        # nums = [11,11,11,22,22,33,33]
        dic = Counter(nums)

        fredic = {}
        for freq in range(len(nums)+1):
            fredic[freq] = []

        for v,i in dic.items():
            # print(v,i)
            if i in fredic:
                fredic[i].append(v)

        answer = []
        for i in range(len(fredic)-1, -1, -1):
            for number in fredic[i]:
                answer.append(number)
                k-=1
                if k==0:
                    return answer

        