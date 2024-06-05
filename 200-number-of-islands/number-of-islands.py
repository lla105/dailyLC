class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return None

        def dfs(grid,i,j):

            if i>=len(grid) or j>=len(grid[0]):
                return 
            if i<0 or j<0 :
                return
            # if grid[i][j]=='0':
            if grid[i][j] != '1':
                return
            grid[i][j] = "99"
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            return 


        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    islands += 1
        return islands