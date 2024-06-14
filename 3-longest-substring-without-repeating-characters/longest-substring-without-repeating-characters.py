class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        stack = []
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            else:
                while s[i] in stack:
                    stack.pop(0)
                stack.append(s[i])
            longest = max(longest, len(stack))
        return longest