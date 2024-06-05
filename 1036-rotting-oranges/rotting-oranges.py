class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get all rotten cells i,j. put in a q.
        # while q, for loop through direction
        # append minutespassed for each while iternation
        minutespassed = 0
        freshcount=0
        if grid is None: 
            return -1
        rottenq = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenq.append( (i,j) )
                elif grid[i][j] == 1:
                    freshcount +=1 
        print(rottenq)
        directions = [ (0,1), (1,0), (0,-1), (-1,0)]
        while rottenq and freshcount >0:
            minutespassed += 1
            for each in range(len(rottenq)):
                x,y = rottenq.popleft()
                print(x,y )
                for dx,dy in directions:
                    i = dx+x
                    j = dy+y
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j]==2 or grid[i][j]==0:
                        continue
                    # if grid[i][j] == 1:
                    freshcount -=1 
                    grid[i][j] = 2
                    rottenq.append( (i,j) )
        # return minutespassed
        if freshcount==0: 
            return minutespassed
        else:
            return -1