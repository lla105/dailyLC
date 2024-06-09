class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        self.isTrue = False
        def bfs(board,i,j,index):
            if index == len(word):
                self.isTrue = True
                return
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return 
            if index >= len(word):
                return
            if board[i][j] != word[index] :
                return
            temp = board[i][j]
            board[i][j] = '#'
            # visited.add( (i,j) )
            bfs(board,i+1,j,index+1)
            bfs(board,i,j+1,index+1)
            bfs(board,i-1,j,index+1)
            bfs(board,i,j-1,index+1)
            board[i][j] = temp
            return
        #find starts
        startlist = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    startlist.append( (i,j) )
        # bfs from each start node
        newboard = board
        for i,j in startlist:
            # visited = set()
            bfs(board,i,j,0)
        return self.isTrue

            
