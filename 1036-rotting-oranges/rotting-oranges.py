class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshcount = 0
        rottencellsQ = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    freshcount +=1
                if grid[i][j] == 2:
                    rottencellsQ.append( (i,j) )
        minutepassed = 0
        directions = [ (0,1),(0,-1), (1,0), (-1,0) ]
        while freshcount and rottencellsQ:
            minutepassed += 1
            for _ in range(len(rottencellsQ)):
                x,y = rottencellsQ.popleft()
                for dx,dy in directions:
                    i = x+dx
                    j = y+dy
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j]!=1:
                        continue
                    rottencellsQ.append( (i,j) )
                    grid[i][j] = 2
                    freshcount -= 1
        
        if freshcount >0:
            return -1
        else:
            return minutepassed