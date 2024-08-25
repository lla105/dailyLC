class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def bruteforce( curList , index ) :
            self.result.append(curList)
            for i in range( index, len(nums)):
                bruteforce( curList+[nums[i]] , i+1 )
        bruteforce( [] , 0 )
        return self.result