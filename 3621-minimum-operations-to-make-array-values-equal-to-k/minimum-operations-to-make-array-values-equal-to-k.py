class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        min_num = float('inf')
        for num in nums:
            min_num = min(min_num, num)
            s.add(num)
        if min_num < k :
            return -1
        same_min = False
        if min_num == k :
            same_min = True
        output = len(s)
        if same_min :
            output -= 1
        return output
