class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set() # format : { (i,j) , (i2,j2) }

        m = len(matrix)
        n = len(matrix[0])
        count = 0
        i = 0
        j = 0
        mat = matrix
        path = []
        # while (i+1,j) not in visited or (i,j+1) not in visited or (i-1,j) not in visited or (i,j-1) not in visited:
        while len(path) < m*n:
            # right 
            while j < n and (i,j) not in visited:
                path.append(mat[i][j])
                visited.add( (i,j) )
                j+=1
            i+=1
            j-=1
            #down
            while i < m and (i,j) not in visited:
                path.append(mat[i][j])
                visited.add( (i,j) )
                i+=1
            i-=1
            j-=1
            #left
            while j>=0 and (i,j) not in visited:
                path.append(mat[i][j])
                visited.add( (i,j) )
                j-=1
            j+=1
            i-=1
            #up
            while i>=0 and (i,j) not in visited:
                path.append(mat[i][j])
                visited.add( (i,j) )
                i-=1
            i+=1
            j+=1
        return path