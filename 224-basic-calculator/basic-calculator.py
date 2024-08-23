class Solution:
    def calculate(self, s: str) -> int:
        def getsign(char):
            if char=="+":
                return 1
            else:
                return -1

        sign = 1
        stack = []
        result = 0
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-':
                result += (num*sign)
                sign = -1 if c == '-' else 1
                num = 0
            elif c=='(':
                stack.append(result)
                stack.append(sign)
                result=0
                num=0
                sign = 1
            elif c==')':
                # tempresult = result+ (num*sign)
                result += (num*sign)
                sign = stack.pop()
                num = stack.pop()
                result = (result*sign) + num
                num = 0

        return result+num*sign