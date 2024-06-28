class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0

        def bfs(grid, i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return
            if grid[i][j]!='1':
                return
            grid[i][j] = '#'
            bfs(grid,i+1,j)
            bfs(grid,i,j+1)
            bfs(grid,i-1,j)
            bfs(grid,i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(grid,i,j)

        return count
