class Solution:
    def isValid(self, s: str) -> bool:
        bracketsdic = {'(': ')',
                        '{': '}',
                        '[': ']'
                        }
        stack = []
        for b in s:
            if b in bracketsdic:
                # open bracket
                stack.append(b)
            else:
                # close bracket
                if len(stack) == 0:
                    return False
                else:
                    prevbracket = stack.pop()
                    print(f'{b} vs {bracketsdic[prevbracket]}')
                    if b != bracketsdic[prevbracket]:
                        return False
                        
        if len(stack)==0:
            return True
        else:
            return False
            