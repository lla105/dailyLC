class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor = image[sr][sc]
        # if image[sr][sc] 
        if originalcolor == color:
            return image
        def bfs(image,i,j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return
            # if image[i][j] == 0:
            #     return
            if image[i][j] != originalcolor:
                return
            print(i,j, image[i][j])
            image[i][j] = color
            bfs(image,i+1,j)
            bfs(image,i-1,j)
            bfs(image,i,j+1)
            bfs(image,i,j-1)

        bfs(image,sr,sc)
        return image