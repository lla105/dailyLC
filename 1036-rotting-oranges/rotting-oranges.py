class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        # def flood(grid,i,j):
        #     #bound check
        #     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
        #         return
        #     if grid[i][j] != 1:
        #         return
        #     grid[i][j] = 2
        #     rottencells.append( (i,j) )
        #     flood(grid,i+1,j)
        #     flood(grid,i,j+1)
        #     flood(grid,i-1,j)
        #     flood(grid,i,j-1)

        #get starting rotten cells
        rottencells = deque()
        freshoranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottencells.append( (i,j) )
                if grid[i][j] == 1:
                    freshoranges += 1

        minutesPassed = 0
        directions = [ (1,0), (-1,0), (0,1), (0,-1) ]
        while rottencells and freshoranges>0:
            # print(rottencells)
            minutesPassed += 1
            for _ in range(len(rottencells)):
                x,y = rottencells.popleft()
                for dx,dy in directions:
                    i = x+dx
                    j = y+dy
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                        continue
                    if grid[i][j] != 1:
                        continue
                    grid[i][j] = 2
                    freshoranges -= 1
                    rottencells.append( (i,j) )

        
        if freshoranges >0:
            return -1
        else:
            return minutesPassed

                
