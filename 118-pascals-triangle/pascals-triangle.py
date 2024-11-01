class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        first = [1]
        second = [1,1]
        output = []
        output.append(first)
        output.append(second)
        for i in range(2,numRows):
            arr = [1]* (i+1)
            print(arr)
            for j in range(1,i):
                prevval1 = output[-1][j-1] 
                prevval2 = output[-1][j]
                arr[j] = prevval1 + prevval2
            output.append(arr)
        return output