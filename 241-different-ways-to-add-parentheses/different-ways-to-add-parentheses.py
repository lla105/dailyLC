class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        output = []
        exp = expression
        def dfs( arr ) :
            templist = []
            for i in range(len(arr)):
                char = arr[i]
                if char not in '+-*':
                    continue
                left = dfs( arr[:i] )
                right = dfs( arr[i+1:])
                for num1 in left:
                    for num2 in right:
                        if char == '+':
                            tempnum = int(num1)+int(num2)
                        elif char=='-':
                            tempnum = int(num1)-int(num2)
                        elif char=='*':
                            tempnum = int(num1)*int(num2)
                        templist.append(tempnum)
            if not templist:
                return [int(arr)]
            return templist

        return dfs( exp )