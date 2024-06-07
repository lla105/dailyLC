class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = {} # format : { (num:index) , (num:index) ....}
        for i in range(len(nums)):
            d[nums[i]] = i
        print(d)
        for i,v in d.items():
            if target==i:
                return v
        return -1