class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print('?k')
        for i in range(len(s)):
            if s[i] in '({[' :
                stack.append(s[i])
            # elif s[i] in ')}]':
            elif False:
                print()
            else:
                if not stack:
                    return False
                if s[i] == ')' and stack[-1]=='(':
                    stack.pop()
                elif s[i] == '}' and stack[-1]=='{':
                    stack.pop()
                elif s[i] == ']' and stack[-1]=='[':
                    stack.pop()
                else:
                    # print(' false in loop. s[i] : ', s[i])
                    return False
        if stack :
            return False
        else:

            return True