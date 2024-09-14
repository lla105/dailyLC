# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         best = [ 0,0 ] # [ num, maxlength]
#         curbest = [0,0]

#         for i in range(len(nums)):
#             if i==0:
#                 curbest = [ nums[i] , 1 ]
#                 continue
#             if nums[i] == curbest[0] :
#                 curbest[1] += 1
#             elif nums[i] < curbest[0] :
#                 if curbest[1] 
class Solution(object):
    def longestSubarray(self, nums):
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans