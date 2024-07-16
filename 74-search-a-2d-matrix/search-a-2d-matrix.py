class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if len(matrix[0]) == 1 and matrix[0][-1]==target:
            return True
        for row in range(len(matrix)):
            head = matrix[row][0]
            tail = matrix[row][-1]
            if head<=target<=tail:
                # print(matrix[row], head,target,tail)
                l = 0
                r = len(matrix[0])-1
                while l<=r:
                    m = (l+r) // 2
                    # print(l,m,r)
                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] < target:
                        l = m+1
                    else:
                        r = m-1


        return False