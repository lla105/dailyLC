class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter ={}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        for key,val in counter.items():
            heapq.heappush(heap, (-val, key))
        res = []

        while len(res) < k:
            temp = heapq.heappop(heap)[1]
            res.append(temp)

        return res