class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1 
        heapq.heapify(nums)
        result = 0
        count = 0
        while count < k:
            temp = -1*(heapq.heappop(nums) )
            result += temp
            count += 1
            newnum = ceil(temp/3)
            newnum = -1* newnum
            heapq.heappush( nums, newnum )

        return result