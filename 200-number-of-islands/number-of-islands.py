def dfs(grid, i , j ):
    # print('test')
    if i<0 or j<0:
        print("a)")
        return
    if i>=len(grid) or j>=len(grid[0]):
        print("b)")
        return
    if grid[i][j]!='1':
        print("c)")
        return
    # if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
    #     return
    grid[i][j] = '#'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end = '')
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
            print("")
        return count