class Solution:
    def calculate(self, s: str) -> int:
        num = 0 
        cursum = 0
        sign = 1
        stack = []
        def getsign(char) :
            if char=='-' :
                return -1
            return 1
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-' :
                cursum += (sign*num)
                num = 0
                sign = getsign(c)
            elif c == '(':
                stack.append( (cursum,sign) )
                sign = 1
                cursum = 0
                num = 0
            elif c== ')':
                insidesum = cursum + (sign*num)
                oldsum , oldsign = stack.pop()
                cursum = oldsum + (oldsign*insidesum)
                num = 0
                sign = 0
        return cursum + (sign*num)