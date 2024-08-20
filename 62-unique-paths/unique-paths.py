class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            row = [0] * n
            grid.append(row)
        def printgrid(grid):
            return
            # for i in range(m):
            #     for j in range(n):
            #         print(grid[i][j] , end=',')
            #     print()
        for i in range(m):
            for j in range(n):
                if i==0:
                    grid[i][j] = 1
                grid[i][0] = 1
        printgrid(grid)
        print()
        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        printgrid(grid)


        return grid[-1][-1]