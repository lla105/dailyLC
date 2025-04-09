class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        for num in nums:
            s.add(num)
        min_num = min(s)
        if min_num < k :
            return -1
        same_min = False
        if min_num == k :
            same_min = True
        max_heap = []
        for num in s:
            heapq.heappush(max_heap, -num)
        output = 0
        while max_heap :
            output += 1
            heapq.heappop(max_heap)
        if same_min :
            output -= 1
        return output
