class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        highest = 0
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i] , 0 ) + 1

        print(d)
        answer = 0
        for i,v in d.items():
            print(i,v)
            if highest < v:
                print('update ')
                highest = v
                answer = i
        return answer