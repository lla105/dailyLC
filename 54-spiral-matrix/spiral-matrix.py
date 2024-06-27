class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def printmatrix(matrix):
            print()
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    print(matrix[i][j], end='  ')
                print()
        n = len(matrix)
        m = len(matrix[0])
        
        if len(matrix[0])==1:
            result = []
            for i in range(len(matrix)):
                result.append(matrix[i][0])
            return result
        if len(matrix) ==1 :
            result = []
            for i in range(len(matrix[0])):
                result.append(matrix[0][i])
            return result
        top=0
        left=0
        right=m
        bottom = n
        starti=0
        startj=0
        cellcount = 0

        result = []
        while len(result) < m*n:
        # while matrix[starti][startj] != "#" or top<bottom or left<right:
            for i in range(right):
                if matrix[top][i] != '#':
                    result.append(matrix[top][i])
                matrix[top][i] = '#'
            top+=1
            # down
            for i in range(bottom):
                if matrix[i][right-1] != '#':
                    result.append(matrix[i][right-1])
                matrix[i][right-1] = '#'
            right -= 1
            # left
            for i in range(right-1, left-1, -1):
                if matrix[bottom-1][i] != '#':
                    result.append(matrix[bottom-1][i])
                matrix[bottom-1][i] = '#'
            bottom -= 1
            # up
            print(bottom,top,'...')
            for i in range(bottom-1, top, -1):
                print(i,left)
                if matrix[i][left] != '#':
                    result.append(matrix[i][left])
                matrix[i][left] = '#'
                starti = i
                startj = left+1
            left += 1
            print('starti and j : ', starti, startj)

        printmatrix(matrix)
        print(' RESULT : ', result)
        return result