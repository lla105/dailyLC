class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        # print(d)
        
        heap = []

        for num,freq in d.items():
            heapq.heappush(heap, (-freq, num))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res