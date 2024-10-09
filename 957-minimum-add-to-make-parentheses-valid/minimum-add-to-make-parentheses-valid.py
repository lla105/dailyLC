class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char=='(':
                stack.append(char)
            else:
                if not stack:
                    count +=1
                else:
                    stack.pop()

        return count+len(stack)