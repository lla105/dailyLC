class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if not stack:
                stack.append( char )
                continue
            if char =='B':
                if stack[-1]=='A':
                    stack.pop()
                else:
                    stack.append(char)
            elif char=='D':
                if stack[-1]=='C':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        print('??')
        return len(stack)