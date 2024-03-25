class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def runbfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 
            if grid[i][j] != '1':
                return
            grid[i][j] = '#'
            runbfs(grid,i+1,j)
            runbfs(grid,i,j+1)
            runbfs(grid,i-1,j)
            runbfs(grid,i,j-1)
            # return


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(grid[i][j],end='')
                if grid[i][j] == '1':
                    runbfs(grid, i , j)
                    count += 1
            print("")

        return count