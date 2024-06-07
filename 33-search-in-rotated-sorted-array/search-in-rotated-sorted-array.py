class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # d = {} # format : { (num:index) , (num:index) ....}
        # for i in range(len(nums)):
        #     d[nums[i]] = i
        # for i,v in d.items():
        #     if target==i:
        #         return v
        # return -1
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            print(l,m,r)
            if nums[l] <= nums[m] : #check if left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m-1
                else: 
                    l = m+1
            else: #check if right side is sorted
                if nums[m] < target <=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
