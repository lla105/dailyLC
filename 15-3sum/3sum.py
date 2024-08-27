from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        result = []

        # Iterate through the array, fixing one element at a time
        for i in range(len(nums)):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers: one starting right after the fixed element and one at the end
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer and avoid duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Move the right pointer and avoid duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif current_sum < 0:
                    # If the sum is too small, move the left pointer to increase the sum
                    left += 1
                else:
                    # If the sum is too large, move the right pointer to decrease the sum
                    right -= 1

        return result
