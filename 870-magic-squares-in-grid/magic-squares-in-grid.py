class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        nononumbers = {0,10,11,12,13,14}
        def checksum(i, j):
            # Extract the 3x3 grid
            s = set()
            for x in range(3):
                for y in range(3):
                    num = grid[i + x][j + y]
                    if num < 1 or num > 9 or num in s:
                        return False
                    s.add(num)
            
            # Check rows and columns
            for x in range(3):
                if sum(grid[i + x][j:j + 3]) != 15:
                    return False
                if sum(grid[i + y][j + x] for y in range(3)) != 15:
                    return False
            
            # Check diagonals
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2] != 15:
                return False
            
            return True


        for i in range( len(grid)-2 ):
            for j in range( len(grid[0]) -2 ):
                if checksum(i,j):
                    print(' 1')
                    result += 1
                else:
                    print(' 2')
        return result