class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [11,11,11,22,22,22,33]

        length = len(nums)
        if length == 1:
            return [nums[0]]

        # d format = { num : frequency }
        d1 = Counter(nums)
        print(f'd1 : {d1}')
        # d2 format = {freq : [num, num]}
        # lets say nums = 4
        # d2 = { 4:[], 3:[], 2:[11,22], 1:[33] }
        # eg nums = [ 11,11,22,22]
        # { 2 : [11,22] }

        d2 = {}
        for i in range(length, 0, -1):
            d2[i] = []
        print(f'd2 : {d2}')

        for i,v in d1.items():
            if v in d2:
                d2[v].append(i)
        print(f'd2 now: {d2}')

        result = []
        kcount = 0
        for i in range(length, 0,-1):
            # print(i)
            for j in d2[i]:
                result.append(j)
                kcount += 1
                if kcount == k:
                    return result
        return result
