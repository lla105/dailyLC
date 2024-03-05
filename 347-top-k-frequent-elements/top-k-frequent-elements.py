class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums = [1,1,1,2,2,3,3,3,3]
        # nums = [2,3,4,1,4,0,4,-1,-2,-1]

        d = Counter(nums)
        print(d)
        heap = []

        for num,freq in d.items():
            heapq.heappush(heap, (-freq, num))

        print(heap)
        res = []
        print()
        for _ in range(k):
            _, num = heapq.heappop(heap)
            print(_, num)
            res.append(num)
        return res