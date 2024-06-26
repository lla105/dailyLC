class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(startindex, path):
            self.result.append(path[:])

            for i in range(startindex, len(nums)):
                path.append(nums[i])

                backtrack(i+1, path )
                path.pop()
        backtrack(0, [])
        return self.result