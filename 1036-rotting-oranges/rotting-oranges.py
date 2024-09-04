class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenq = deque() 
        fresh = 0 
        minutespassed = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] == 2:
                    rottenq.append( (i,j) )
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [ (1,0), (0,1), (-1,0), (0,-1) ]
        while rottenq and fresh :
            minutespassed += 1
            for _ in range(len(rottenq)):
                x,y = rottenq.popleft()
                for dx,dy in directions:
                    i = x+dx
                    j = y+dy
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j] != 1:
                        continue
                    fresh -= 1
                    grid[i][j] = 2
                    rottenq.append( (i,j) )
        print(fresh , minutespassed)

        if fresh==0:
            return minutespassed
        else:
            return -1