class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target  and target<= matrix[i][-1]:
                mat = matrix[i]
                l = 0
                r = len(mat) -1 
                while l<=r:
                    m = (l+r)//2
                    if mat[m]==target:
                        return True
                    elif mat[m]>target:
                        r = m - 1
                    else:
                        l = m+1
        return False