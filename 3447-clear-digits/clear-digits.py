class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit() and stack:
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)