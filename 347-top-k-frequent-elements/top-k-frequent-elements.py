class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        # print(d)
        nums = [5,3,1,1,1,3,73,1]

        heap = []

        for num,freq in d.items():
            heapq.heappush(heap, (-freq, num))

        print(" heap : ", heap )
        res = []

        for _ in range(k):
            temp = heapq.heappop(heap)[1]
            print("temp : ", temp)
            res.append(temp)
        # for i in range(k):
        #     res.append(heap[i][1])

        return res