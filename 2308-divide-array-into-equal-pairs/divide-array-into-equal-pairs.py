class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        # print(d)
        for i,v in d.items():
            # print(v,'//','2','=', v//2)
            if v%2 != 0:
                return False
        return True