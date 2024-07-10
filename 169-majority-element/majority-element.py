class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        highest = 0
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i] , 0 ) + 1

        print(d)
        answer = 0
        for i,v in d.items():
            if highest < v:
                highest = v
                answer = i
        return answer