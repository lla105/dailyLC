class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mathshit = ["+","-","*","/"]

        for i in range(len(tokens)):
            t = tokens[i]
            if t in mathshit:
                num2 = stack.pop()
                num1 = stack.pop()
                if t=="+":
                    stack.append( int(num1+num2) )
                elif t=="-":
                    stack.append( int(num1-num2) )
                elif t=='*':
                    stack.append( int(num1*num2) )
                else:
                    stack.append( int(num1/num2) )
            else:
                stack.append(int(t))
        return stack[-1]