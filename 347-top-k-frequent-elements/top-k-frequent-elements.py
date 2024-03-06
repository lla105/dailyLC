class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [5,3,1,1,1,3,73,1]
        counter = Counter(nums)
        heap = [(v,k) for (k,v) in counter.items()]
        # heap = []
        # for k,v in counter.items():
        #     heap.append( (v,k))

        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        return [num for (freq, num) in heap]
        # answer = []
        # for freq,num in heap :
        #     answer.append(num)

        # return answer