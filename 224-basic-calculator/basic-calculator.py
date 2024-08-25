class Solution:
    def calculate(self, s: str) -> int:
        def getsign(char):
            if char == '+':
                return 1
            return -1
        tempnum = 0
        cursum = 0
        sign = 1
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                tempnum = tempnum*10 + int(char)
            elif char in '+-':
                cursum += (sign*tempnum)
                tempnum = 0
                sign = getsign(char)
            elif char == '(' :
                stack.append(cursum)
                stack.append(sign)
                cursum = 0
                sign = 1
                tempnum = 0
            elif char == ')' :
                insidesum = cursum + (sign*tempnum)
                prevsign = stack.pop()
                prevsum = stack.pop()
                cursum = prevsum + (prevsign*insidesum)
                tempnum = 0
                

# s= '2-1+(2-3)
        return cursum + (sign*tempnum)

