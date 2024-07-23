class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')
                else:
                    q.append( (i,j) )
        directions = [ (0,1), (0,-1), (1,0), (-1,0) ]
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                i = x+dx
                j = y+dy
                if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]):
                    continue
                if mat[i][j] == 0:
                    continue
                if mat[i][j] > mat[x][y]+1:
                    mat[i][j] = mat[x][y] + 1
                    q.append( (i,j) )
                # if mat[i][j]!=0:
                #     mat[i][j] = min(mat[x][y]+1 , mat[i][j])
                #     q.append( (i,j) )
        return mat


        # if not mat:
        #     return mat
        # visited = set()
        # def bfs(mat,i,j):
        #     if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]):
        #         return float('inf')
        #     if mat[i][j] == 0 or (i,j) in visited:
        #         return 1
        #     visited.add( (i,j) )
        #     right = bfs(mat,i+1,j)
        #     left = bfs(mat,i-1,j)
        #     up = bfs(mat,i,j+1)
        #     down = bfs(mat,i,j-1)
        #     minpath = min( right, left, up, down )
        #     # print(' >> ', math[i][j], 'min path: ', minpath)
        #     mat[i][j] = mat[i][j] + minpath 
        #     return float('inf')

        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j]==1:
        #             bfs(mat,i,j)

        # return mat