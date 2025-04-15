class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append( (i,j) )
                else:
                    mat[i][j] = -1
        # print(q)
        dir = [ (1,0), (0,1), (-1,0), (0,-1) ]
        visited = set()
        while q:
            x,y = q.popleft()
            for dx, dy in dir:
                i = x+dx
                j = y+dy
                if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]) or (i,j) in visited:
                    continue
                if mat[i][j] < 0 :
                    mat[i][j] = mat[x][y] + 1
                visited.add( (i,j))
                q.append( (i,j) )
        return mat