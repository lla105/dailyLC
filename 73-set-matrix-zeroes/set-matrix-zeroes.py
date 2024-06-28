class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # find starting points
        startingzeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    startingzeros.append( (i,j) )
        print(startingzeros)

        for x,y in startingzeros:
            # for rows
            for col in range(len(matrix[0])):
                matrix[x][col] = 0
            for row in range(len(matrix)):
                matrix[row][y] = 0
        print(matrix)
        return matrix