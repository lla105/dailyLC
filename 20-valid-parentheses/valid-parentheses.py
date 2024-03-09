class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)

        bdic = { ")":"(" , "]":"[", "}":"{"}
        
        for i in range(length):
            char = s[i]
            if char not in bdic:
                # is open bracket
                stack.append(char)
            else:
                #is closed bracket
                if len(stack)==0:
                    # stack empty, is false
                    return False
                else:
                    #stack not empty, check last item
                    if stack[-1]!=bdic[char]:
                        return False
                    else:

                        stack.pop()
            # print(f'{stack}')
                
        if len(stack)==0:
            return True
        else:
            return False

            