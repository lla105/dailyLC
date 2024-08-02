class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # Edge cases
        if total_ones == 0 or total_ones == n:
            return 0
        
        # Create doubled array and cumulative sum
        doubled_nums = nums + nums
        cumulative_sum = [0] + list(accumulate(doubled_nums))
        
        max_ones_in_window = 0
        
        # Check all possible windows of size total_ones
        for i in range(n + 1):
            ones_in_window = cumulative_sum[i + total_ones] - cumulative_sum[i]
            max_ones_in_window = max(max_ones_in_window, ones_in_window)
        
        return total_ones - max_ones_in_window
