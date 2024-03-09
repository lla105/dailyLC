class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the rows
        s = set()

        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[i][j]
                if cell in s:
                    # print(">>>",cell, s)
                    return False
                else :
                    if cell !='.':
                        s.add(cell)
        print(f' rows are cool')

        # check the cols
        for i in range(9):
            s = set()
            for j in range(9):
                cell = board[j][i]
                if cell in s:
                    # print(">>>",cell, s)
                    return False
                else :
                    if cell !='.':
                        s.add(cell)
        print(f' cols are cool')

        # check each mini 3x3 grid

        anchors = [ (0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)
                    ]
        for a in anchors:
            s = set()
            for i in range(a[0], a[0]+3):
                for j in range(a[1], a[1]+3):
                    # print(f'({i},{j})')
                    cell = board[i][j]
                    if cell in s:
                        return False
                    else:
                        if cell !='.':
                            s.add(cell)
                # print("---------")
        return True