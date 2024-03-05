class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check the rows

        for i in range(9): # row
            s = set()
            for j in range(9): # cols
                cellValue = board[i][j]
                if cellValue in s:
                    return False
                else:
                    if cellValue !='.':
                        s.add(cellValue)
        print("rows are cool")      
        #  check the cols
        for i in range(9): #row
            s = set()
            for j in range(9): #cols
                cellValue = board[j][i]
                if cellValue in s:
                    return False
                else:
                    if cellValue !='.':
                        s.add(cellValue)

        print("cols are cool")
        # check the 3x3 grids each
        anchors = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]


        for ij in range(9):
            s = set()
            x = anchors[ij][0]
            y = anchors[ij][1]
            for i in range(x, x+3):
                for j in range(y, y+3):
                    # print(">> ",i,j , " vs ", anchors[ij])
                    cellValue = board[j][i]
                    if cellValue in s:
                        return False
                    else:
                        if cellValue != '.':
                            s.add(cellValue)

        return True
                    