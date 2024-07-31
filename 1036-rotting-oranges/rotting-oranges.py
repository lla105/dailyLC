class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute= 0
        rottencells = deque()
        freshcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottencells.append( (i,j) )
                elif grid[i][j] == 1:
                    freshcount += 1
        directions = [ (0,1),(0,-1),(1,0),(-1,0) ]
        while freshcount>0 and rottencells:
            minute+=1
            for _ in range(len(rottencells)):
                x,y = rottencells.popleft()
                for dx,dy in directions:
                    i = x+dx
                    j = y+dy
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j] != 1:
                        continue
                    freshcount-=1
                    grid[i][j] = 2
                    rottencells.append( (i,j) )

        if freshcount>0:
            return -1
        else:
            return minute