class Solution:
    def calculate(self, s: str) -> int:
        # s = '12-(3+4)'
        def getsign(char):
            if char=='-':
                return -1
            return 1
        num = 0
        cursum = 0
        sign = 1
        stack = []
        operators = ("+", "-")
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            elif char in operators:
                cursum += int(num*sign)
                sign = getsign(char)
                num = 0
            elif char == '(':
                stack.append( int(cursum) )
                if sign==1: 
                    stack.append('+')
                if sign==-1: 
                    stack.append('-')
                num = 0
                cursum = 0
                sign = 1
            elif char == ')' :
                cursum += int(num*sign)
                oldsign = stack.pop()
                oldsum = stack.pop()
                # print('>> ', oldsum, oldsign, cursum)
                if oldsign=='+':
                    newsign = 1
                else:
                    newsign = -1
                num = cursum
                cursum = oldsum
                sign = newsign
                # cursum = int(oldsum) + int(newsign*cursum)

        #stack = [ 12, '-']

        answer = cursum + (num*sign)
        return answer
        # 11 + 12 - ( 3 + 4 )
        # num = 1
        # num = 11 
        # cursum = 11, num = 0, sign = 1 
        # num = 1
        # num = 12
        # result = cursum + (num*sign)
        # sign = 1, + 
        # stack.append(result), stack.append('+'), num=0, result = 0, sign=1
        # ... 
        # result = 7 = result(3) + (num*sign)
        # ). stack.pop->sign. stack.pop->(prevresult). result=(result*sign)+prevresult

