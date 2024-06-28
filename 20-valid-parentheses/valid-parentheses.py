class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in range(len(s)):
            if s[i] in d: # is closed bracket
                if not stack:
                    print('  2) stack is empty')
                    return False
                if stack[-1]!= d[s[i]]:
                    print('    3) bracket mismatch')
                    return False
                stack.pop()
            else:
                # is open bracket
                stack.append(s[i])
        if len(stack)==0:
            return True
        else:
            return False