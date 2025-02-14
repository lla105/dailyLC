class Solution:
    # def findvalue( arr ) :
    #     left = 0
    #     right = len(arr)-1
    #     while left < right :
    #         m = ()
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        count = 0
        prod = 1
        left = 0
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left +=1
            count += right - left + 1
        return count
        # # q = queue() # [ 10, 5 ]
        # l = 0
        # # r = 1
        # output = []
        # curprod = nums[l]
        # extras = 0
        # dp = []
        # for i in range(len(nums)):
        #     num = nums[i]
        #     if num < k:
        #         output.append( [num] )
        # if not output:
        #     return 0
        # for r in range(len(nums)):
        #     if r == 0:
        #         continue
        #     num = nums[r]
        #     curprod = curprod * num
        #     # while curprod >= k and l<r:
        #     #     curprod=curprod/nums[l]
        #     #     l+=1
        #     if curprod >= k:

        #     if l<r:
        #         output.append( nums[l:r+1] )
        #     if r-l>=2:
        #         extras += (r-l-1)
        #     # ll = l
        #     # while ll<r:
        #     #     output.append( nums[ll:r+1] )
        #     #     ll+=1
        # for each in output:
        #     print(each)
        # return len(output)+extras

