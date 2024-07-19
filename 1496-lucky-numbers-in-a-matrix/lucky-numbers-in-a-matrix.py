class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def printgrid(m):
            for i in range(len(m)):
                for j in range(len(m[0])):
                    num = m[i][j]
                    if num > 10:
                        print(m[i][j], end=', ')
                    else:
                        print(m[i][j], end=',  ')
                print()
        m = matrix
        printgrid(m)
        print()
        # minnums = []
        d = {} # format : { num: (i,j) }
        for i in range(len(m)):
            lowest=float('inf')
            ij = (0,0)
            for j in range(len(m[0])):
                if m[i][j] < lowest:
                    lowest = m[i][j]
                    ij = (i,j)
            d[lowest] = ij

        print(d)
        result = []
        for num, ij in d.items():
            i = ij[0]
            j = ij[1]
            isLargest = True
            for rowindex in range(len(m)):
                if num<m[rowindex][j]:
                    isLargest = False
            if isLargest:
                result.append(num)
        return result
        return [99]
        # 3,6
        # 7,1
        # 5,2
        # 4,8