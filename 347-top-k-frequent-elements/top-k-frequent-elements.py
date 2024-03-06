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
        print("dic: ", dic)

        fredic = {}
        for freq in range(len(nums)+1):
            fredic[freq] = []
        print("fredic : ", fredic)

        for v,i in dic.items():
            # print(v,i)
            if i in fredic:
                fredic[i].append(v)
        print(fredic)

        answer = []
        for i in range(len(fredic)-1, -1, -1):
            print("i:", i)
            for number in fredic[i]:
                print(">>>", number)
                answer.append(number)
                k-=1
                if k==0:
                    return answer

        