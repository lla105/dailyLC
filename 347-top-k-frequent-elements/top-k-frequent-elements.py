class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums = [4,4,4,5,5,6]
        # nums = [2,3,4,1,4,0,4,-1,-2,-1]
        d = Counter(nums)
        print(d)
        heap = []
        for each in d:
            # print(each)
            heapq.heappush(heap, (-d.get(each) , each ))

        print("heap : ", heap)
        answer = []
        print()
        # for i in range(k):
        #     print(heap[i][1])
        #     answer.append(heap[i][1])

        for _ in range(k):
            _, num = heapq.heappop(heap)
            answer.append(num)

        return answer