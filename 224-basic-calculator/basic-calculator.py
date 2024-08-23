class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curnum = 0
        sign = 1
        result = 0
        def getsign(char):
            if char=='+':
                return 1
            else:
                return -1
        for i in range(len(s)):
            c = s[i]
            if c.isdigit() : 
                curnum = curnum*10 + int(c)
            elif c in '+-' : 
                result += curnum*sign
                curnum = 0
                sign = getsign(c)
            elif c=='(':
                stack.append(result)
                stack.append(sign)
                result = 0
                curnum = 0
                sign = 1
            elif c == ')':
                result += curnum*sign
                sign = stack.pop()
                prevnum = stack.pop()
                result = (result*sign) + prevnum
                curnum = 0                
        return result+ curnum*sign
