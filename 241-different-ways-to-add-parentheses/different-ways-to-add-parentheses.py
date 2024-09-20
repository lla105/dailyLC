class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def bf( arr ):
            self.diffWaysToCompute( arr )
        output = []
        exp = expression
        for i in range(len(exp)):
            op = exp[i]
            if op not in '+-*':
                continue
            # left  = bf( exp[ :i] )
            # right = bf( exp[i+1:] )
            left = self.diffWaysToCompute( exp[0:i] )
            right = self.diffWaysToCompute( exp[i+1: ] )
            for i in left:
                for j in right:
                    if op == '*':
                        output.append( int(i)*int(j) )
                    elif op=='+':
                        output.append( int(i)+int(j) )
                    elif op=='-':
                        output.append( int(i)-int(j) )
        if not output:
            output.append(int(exp))
        return output