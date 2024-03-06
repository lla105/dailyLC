class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        # print(d)
        
        heap = []

        for num,freq in d.items():
            heapq.heappush(heap, (-freq, num))

        res = []

        for _ in range(k):
            temp = heapq.heappop(heap)[1]
            print("temp : ", temp)
            res.append(temp)

        return res