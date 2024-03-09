class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [11,11,11,22,22,22,33]
       # dictionary format : { value : frequency }

        if len(nums)==1:
           return [nums[0]]
           
        dic1 = Counter(nums)
        print(f"dic1: {dic1}")


        # from 0 to n, where n is len(nums)
        length = len(nums)
        result = []
        count = 0
        dic2 = {}
        for i in range(length, -1,-1):
            # print(f'index : {i}')
            dic2[i] = []
        print(f"dic2 : {dic2}")

        for i,v in dic1.items():
            # print(f'{i}, {v}')
            dic2[v].append(i)
        print(f"new dic2: {dic2}")

        for i in range(length, -1,-1):
            for j in dic2[i]:
                if j in dic1:
                    result.append(j)
                    count += 1
                    if count == k:
                        return result