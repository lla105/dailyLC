class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[i][j]
                if cell in s:
                    return False
                else:
                    if cell!='.':
                        s.add(cell)
        print("row is good")

        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[j][i]
                if cell in s:
                    return False
                else:
                    if cell!='.':
                        s.add(cell)

        print("col is good too")

        anchors = [ (0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6) ]
        
        # traverse 3x3s
        x=0
        y=0
        for eachgrid in range(9):
            z = anchors[eachgrid]
            s = set()
            for i in range(z[0], z[0]+3, 1):
                for j in range(z[1], z[1]+3, 1):
                    cell = board[i][j]
                    if cell in s:
                        return False
                    else:
                        if cell!='.':
                            s.add(cell)
            #         print(i,j)
            # print("===")
        return True