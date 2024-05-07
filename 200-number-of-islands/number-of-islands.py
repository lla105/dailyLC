def runbfs(i,j,grid):
    if i>=len(grid) or j>=len(grid[0]):
        return
    if i<0 or j<0:
        return
    if grid[i][j] != '1':
        return
    grid[i][j] = "#"
    runbfs(i+1, j, grid)
    runbfs(i, j+1, grid)
    runbfs(i-1, j, grid)
    runbfs(i, j-1, grid)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    runbfs(i,j,grid)
                    count += 1

        return count