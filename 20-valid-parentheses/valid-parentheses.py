class Solution:
    def isValid(self, s: str) -> bool:
        # (())
        # ({)
        # ]
        # d = {"(":")",
        #     "{":"}",
        #     "[":"]"
        #     }
        d = {")": "(",
            "]": "[",
            "}": "{"
            }
        stack = []
        length = len(s)
        for i in range(length):
            char = s[i]
            if char in d:
                # is close bracket
                print(f' is closed : {char}')
                if len(stack)!=0 and stack[-1]==d[char]:
                    stack.pop()
                else:
                    return False
            else:
                # is open bracket
                stack.append(char)
        if len(stack)==0:
            return True
        else:
            return False