class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        def bf( curList, index , level):
            print(level*'  ', f'appending curlist: ', curList)
            output.append( tuple(curList) )

            for i in range( index, len(nums)):
                print(level*'  ' , f'[{i}] : {nums[i]}')
                if i>index and nums[i]==nums[i-1]:
                    print(level*'  ', f'3.2) conflict as prev.')
                    continue
                print(level*'  ', f'3.1) calling next: {nums[i]} vs {nums[i-1]} & {i} vs {index}')
                bf( curList+[nums[i]] , i+1 , level+1)
        bf( [], 0 ,0)
        return output