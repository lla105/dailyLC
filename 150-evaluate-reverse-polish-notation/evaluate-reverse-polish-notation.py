class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            t = tokens[i]
            if t not in operations:
                # print('is digit: ', t, stack)
                stack.append(int(t))
            else:
                # print('not digit: ', t, stack)
                num2 = stack.pop()
                num1 = stack.pop()
                if t=='+':
                    stack.append(num2+num1)
                elif t=='-':
                    stack.append(num1-num2)
                elif t=='*':
                    stack.append(num1*num2)
                else:
                    stack.append( int(num1/num2))

            # print(stack)
        print(stack)

        return stack[-1]