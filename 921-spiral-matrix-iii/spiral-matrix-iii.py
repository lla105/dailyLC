class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        outputlist = []
        visited = set()
        totalcells = rows*cols
        steps = 1
        i = rStart
        j = cStart
        outputlist.append( (i,j) )
        # print('start ', i,j, outputlist)
        def addij(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                # print(' out of bound')
                return
            # print(' apepnding : ', i,j)
            outputlist.append( (i,j) )
        while len(outputlist) < totalcells:
            # right
            for step in range(steps):
                j+=1
                addij(i,j)
                # print('right',i,j, outputlist)
            # down
            for _ in range(steps):
                i+=1
                addij(i,j)
                # print('down',i,j, outputlist)
            #left
            steps+=1
            for _ in range(steps):
                j-=1
                addij(i,j)
                # print('left',i,j, outputlist)
            #up
            for _ in range(steps):
                i-=1
                addij(i,j)
                # print('up',i,j, outputlist)
            steps+=1
        return outputlist