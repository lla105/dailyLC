class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # print(boo_arr)
        for i in range(len(matrix)):
            boo_arr = [False] * len(matrix)
            for j in range(len(matrix[0])):
                cell_val = matrix[i][j]
                boo_index = cell_val - 1
                if boo_arr[boo_index] :
                    return False
                boo_arr[boo_index] = True
        print(' good so far? ')
        for i in range(len(matrix)):
            boo_arr = [False] * len(matrix)
            for j in range(len(matrix[0])):
                cell_val = matrix[j][i]
                boo_index = cell_val - 1
                if boo_arr[boo_index] :
                    return False
                boo_arr[boo_index] = True
        return True
