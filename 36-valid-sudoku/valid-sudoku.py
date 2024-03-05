class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            s = set()
            for j in i:
                if j in s:
                    return False
                else:
                    if j!=".":
                        s.add(j)
        print("rows ok")

        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[j][i]
                if cell in s:
                    return False
                else:
                    if cell!=".":
                        s.add(cell)

        print("cols ok")

        anchors = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]

        for grid in range(9):
            s = set()
            i = anchors[grid][0]
            j = anchors[grid][1]
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    # print(">>>", ii, jj)
                    cell = board[ii][jj]
                    if cell in s:
                        return False
                    else:
                        if cell!='.':
                            s.add(cell)
            print("=======")
        return True
