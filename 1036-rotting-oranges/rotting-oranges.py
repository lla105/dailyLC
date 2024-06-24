class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        # get initial rotten cells
        startcells = deque()
        freshcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    startcells.append((i,j))
                if grid[i][j] == 1:
                    freshcount += 1

        minutesPassed = 0
        directions = [ (0,1), (0,-1), (1,0), (-1,0) ]

        while startcells and freshcount > 0 :
            minutesPassed += 1
            for temp in range(len(startcells)):
                x,y = startcells.popleft()
                for dx,dy in directions:
                    i = x+dx
                    j = y+dy
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j] != 1:
                        continue
                    freshcount -=1 
                    startcells.append( (i,j) )
                    grid[i][j] = 2

        if freshcount == 0:
            return minutesPassed
        else:
            return -1