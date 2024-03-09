class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [11,11,11,22,22,22,33]
       # dictionary format : { value : frequency }

        if len(nums)==1:
            return [1]

        # nums = [11,11,11,22,22,33,33]
        dic = Counter(nums)

        fredic = {}
        for freq in range(len(nums)+1):
            fredic[freq] = []

        for v,i in dic.items():
            fredic[i].append(v)

        answer = []
        for i in range(len(fredic)-1, -1, -1):
            for number in fredic[i]:
                answer.append(number)
                k-=1
                if k==0:
                    return answer