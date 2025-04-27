class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # print(boo_arr)
        for i in range(len(matrix)):
            boo_arr = [False] * len(matrix)
            boo_arr_vert = [False] * len(matrix)
            for j in range(len(matrix[0])):
                cell_val = matrix[i][j]
                boo_index = cell_val - 1
                if boo_arr[boo_index] :
                    return False
                boo_arr[boo_index] = True

                cell_val_vert = matrix[j][i]
                boo_index_vert = cell_val_vert - 1
                if boo_arr_vert[boo_index_vert] :
                    return False
                boo_arr_vert[boo_index_vert] = True
        # print(' good so far? ')
        # for i in range(len(matrix)):
        #     boo_arr = [False] * len(matrix)
        #     for j in range(len(matrix[0])):
        #         cell_val = matrix[j][i]
        #         boo_index = cell_val - 1
        #         if boo_arr[boo_index] :
        #             return False
        #         boo_arr[boo_index] = True
        return True
