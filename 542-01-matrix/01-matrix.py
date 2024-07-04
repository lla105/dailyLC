class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [ (0,1), (0,-1), (1,0), (-1,0)]
        m = len(mat)
        n = len(mat[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append( (i,j) )
                if mat[i][j]==1:
                    mat[i][j] = float('inf')

        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                i = x+dx
                j = y+dy
                if i<0 or j<0 or i>=m or j>=n:
                    continue
                if mat[i][j] > mat[x][y] + 1 :
                    mat[i][j] = mat[x][y] + 1 
                    q.append( (i,j) )

        return mat