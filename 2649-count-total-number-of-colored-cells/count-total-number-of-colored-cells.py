class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1 :
            return 1
        four = 4
        output = 1
        for i in range(1,n):
            offset = i
            # if offset==0:
            #     offset = 1:
            output += (offset * 4)
        return output
#  1, 4, 8, 12, 16