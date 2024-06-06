class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return None
        # gather initial rotten i,j
        rottenq = deque()
        freshoranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenq.append( (i,j) )
                elif grid[i][j] == 1:
                    freshoranges += 1
        minutesPassed = 0
        directions = [ (0,1), (1,0), (0,-1), (-1,0) ]
        while rottenq and freshoranges>0:
            minutesPassed += 1
            for index in range(len(rottenq)):
                curx,cury = rottenq.popleft()
                # curx = eachrotten[0]
                # cury = eachrotten[1]
                for dx,dy in directions:
                    i = dx+curx
                    j = dy+cury
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j]==0 or grid[i][j]==2:
                        continue
                    # if grid[i][j]==1:
                    rottenq.append( (i,j) )
                    grid[i][j] = 2
                    freshoranges -= 1
        # return minutesPassed
        if freshoranges==0:
            return minutesPassed
        else:
            return -1


            