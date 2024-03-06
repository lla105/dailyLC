class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        bdic = {")": "(", 
                "}": "{",
                "]": "["
                }
        for b in s:
            if b in bdic:
                # is a closed bracket
                if len(stack)!=0 and stack[-1] == bdic[b]:
                    # is good. pop it off?
                    stack.pop()
                else:
                    return False
            # is a open bracket
            else:
                stack.append(b)
        if len(stack)==0:
            return True
        else:
            return False
