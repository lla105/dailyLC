class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0 :
                    visited.add( (i,j) )
                    q.append( (i,j) )
                else:
                    mat[i][j] = float('inf')

        directions = [ (1,0), (0,1), (-1,0), (0,-1) ]

        while q:
            x,y = q.popleft()
            for dx, dy in directions:
                i = x+dx
                j = y+dy
                if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]):
                    continue
                if (i,j) in visited:
                    continue
                mat[i][j] = min(mat[i][j] , mat[x][y]+1 )
                visited.add( (i,j) )
                q.append( (i,j) )
        return mat