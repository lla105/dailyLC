class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        def reverse(matrix):
            for r in range(len(matrix)):
                left = 0
                right = len(matrix) -1
                while left<right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left+=1
                    right-=1
        transpose(matrix)
        reverse(matrix)
