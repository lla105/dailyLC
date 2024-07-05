class Solution:
    def isValid(self, s: str) -> bool:
        # closed = { '(':')' , '{':'}' , '[':']' }
        closed = { ')':'(' , '}':'{' , ']':'['}
        stack = []

        for i in range(len(s)):
            if s[i] in closed:
                # is closed bracket
                if not stack:
                    return False
                else:
                    if closed[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                # is open bracket
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False