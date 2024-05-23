class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        nums = s
        d = {")" : "(",
            "}" : "{",
            "]" : "["
            }
        if s[0] in d:
            return False
        stack = []

        for i in range(len(s)):
            # print('1. ', stack, '--->', s[i])
            if s[i] in d: # is a closed b
                if len(stack)!=0:
                    if stack[-1]!=d[s[i]]: 
                        #bs don't match stack prev
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else: # is an open b
                stack.append(s[i])
            # print('.  ',stack)
        if len(stack)==0:
            return True
        else:
            return False
                