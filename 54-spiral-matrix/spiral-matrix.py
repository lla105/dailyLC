class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def printmatrix(matrix):
            for i in range(len(matrix)):
                print('[' , end='')
                for j in range(len(matrix[0])):
                    print(matrix[i][j], end='')
                print(']')
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows -1
        left = 0
        right = cols - 1
        result = []
        while len(result) < rows*cols:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <=bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        printmatrix(matrix)
        return result
