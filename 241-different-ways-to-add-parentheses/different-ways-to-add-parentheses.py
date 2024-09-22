class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        output = []
        exp = expression

        def dfs( arr ) :
            curlist = []
            for i in range(len(arr)):
                char = arr[i]
                if char not in '+-*':
                    continue
                left = dfs( arr[ :i] )
                right = dfs( arr[i+1:] )
                print(left, char, right)
                for num1 in left:
                    for num2 in right:
                        if char=='+':
                            tempnum = int(num1) + int(num2)
                        elif char=='-':
                            tempnum = int(num1) - int(num2)
                        elif char=='*':
                            tempnum = int(num1) * int(num2)
                        curlist.append(tempnum)
            if not curlist:
                return [ int(arr) ]
            return curlist            
        return dfs(exp)
        
        # for i in range(len(exp)):
        #     char = exp[i]
        #     if char not in '+-*':
        #         continue
            