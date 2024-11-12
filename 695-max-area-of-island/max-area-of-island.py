class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            left = dfs(i-1,j)
            down = dfs(i,j-1)
            right = dfs(i+1,j)
            up = dfs(i,j+1)
            return ((left+down+right+up) + 1)
            # return 1
        arr = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    arr.append(temp)
        # print(arr)
        # print(max(arr))
        output = 0
        for num in arr:
            output = max(output,num)
        # return max(arr)
        return output
                