class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float('inf')
        # print(mat)
        directions = [ (1,0),(-1,0),(0,1),(0,-1)]
        while q:
            oldi, oldj = q.popleft()
            for di,dj in directions:
                newi,newj = oldi+di,oldj+dj
                # if newi<0 or newj<0 or newi>=m or newj>=n:
                #     continue
                # if mat[newi][newj]==0:
                #     continue
                if 0<=newi<m and 0<=newj<n and mat[newi][newj]>mat[oldi][oldj]+1:
                    mat[newi][newj]=mat[oldi][oldj]+1
                    q.append((newi,newj))
        return mat