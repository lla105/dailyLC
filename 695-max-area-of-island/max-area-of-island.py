def runbfs(i,j,grid, counting):
    if i>=len(grid) or j>=len(grid[0]):
        return 0
    if i<0 or j<0:
        return 0
    if grid[i][j] != 1:
        return 0
    grid[i][j] = 99
    counting = 1

    right = runbfs(i+1,j,grid,counting)
    top = runbfs(i,j+1,grid,counting)
    left = runbfs(i-1,j,grid,counting)
    down = runbfs(i,j-1,grid,counting)

    print(" returning: ", right, top, left, down)
    return right + top + left + down + counting

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tempcount = runbfs(i,j,grid,0)
                    print(">>>", tempcount, "[]",i,j)
                    count = max(count, tempcount)
        print(grid)
        return count 