class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n) != len(original):
            return []
        col = 0 
        temp = []
        grid = []
        for i in range(len(original)):
            temp.append(original[i])
            col +=1
            if col == n :
                col = 0
                grid.append(temp)
                temp = []
        return grid