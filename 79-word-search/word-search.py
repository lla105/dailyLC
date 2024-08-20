class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        m = len(board)
        n = len(board[0])
        def printboard(board):
            return
            # for i in range(m):
            #     for j in range(n):
            #         print(board[i][j], end=' ')
            #     print()
            # print()

        def bfs( curList, index , i, j):
            if len(curList) == len(word):
                # print( ' FOUND IT ')
                self.result = True
                return
            if i<0 or j<0 or i>=m or j>=n:
                return
            if board[i][j] == '#' or board[i][j] != word[index]:
                return
            OGchar = board[i][j]
            board[i][j] = '#'
            printboard(board)
            bfs( curList+[OGchar] , index+1, i+1,j)
            bfs( curList+[OGchar] , index+1, i-1,j)
            bfs( curList+[OGchar] , index+1, i,j+1)
            bfs( curList+[OGchar] , index+1, i,j-1)

            board[i][j] = OGchar
            return

        if not word:
            self.result

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    bfs( [] , 0 , i,j)
        return self.result