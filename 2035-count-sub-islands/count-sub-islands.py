class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])
        self.islands2list = []
        def get2islands( i,j ):
            if i<0 or j<0 or i>=m or j>=n :
                return
            if grid2[i][j] != 1:
                return
            self.curisland.append( (i,j) )
            grid2[i][j] = "#"
            get2islands(i-1,j)
            get2islands(i+1,j)
            get2islands(i,j-1)
            get2islands(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.curisland = []
                    get2islands(i,j)
                    self.islands2list.append( tuple(self.curisland) )
        # print(">>> island count : ", len(self.islands2list))
        count = 0
        for i in range(len(self.islands2list)):
            # print('ISLAND #', i)
            cellmatch = True
            for j in range(len(self.islands2list[i])):
                # print(self.islands2list[i][j] , end='')
                x,y  = self.islands2list[i][j]
                if grid1[x][y] != 1:
                    cellmatch = False
            if cellmatch :
                count += 1
            # print()
        return count
