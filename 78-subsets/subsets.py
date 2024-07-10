class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(curList, available, index):
            if len(curList) > len(nums):
                return
            # print(curList)
            result.append(curList)

            for i in range(index, len(nums)):
                nextavailable = nums[:i] + nums[i+1:]
                # print('next available : ', nextavailable)
                nextList = curList + [nums[i]]
                bt(nextList , nextavailable, i+1)
        bt([] , nums, 0)
        return result