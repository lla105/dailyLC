class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        grid = []
        # print(' s len : ', len(s))
        for i in range(numRows):
            temprow = [ '' ] * ( len(s) )
            grid.append(temprow)
        # for row in grid:
        #     print(row)
        i = 0
        j = 0
        sindex = 0
        # print(' len(grid):', len(grid), ' len(grid[0] ', len(grid[0]))
        while sindex<len(s) :
            # down 
            while sindex < len(s) and i < len(grid) :
                # print('>> ', i)
                grid[i][j] = s[sindex]
                i+=1
                sindex+=1
            i-=2
            j+=1
            while sindex < len(s) and i>0:
                grid[i][j] = s[sindex]
                sindex+=1
                i-=1
                j+=1
        # for row in grid:
        #     print(row)
        output_string = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '':
                    output_string += grid[i][j]
        return output_string

# len(s) = 14 -> need 7 cols
# len(s) = 14 -> need 7 cols