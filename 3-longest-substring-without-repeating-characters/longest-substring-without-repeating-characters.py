class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        stack = deque()
        sdic = {}
        maxlength = 0
        for i in range(len(s)):
            if not stack or i == 0 :
                stack.append(s[i])
                sdic[s[i]] = 1
                continue
            if s[i] in sdic:
                # repeating somwhere in stack
                while stack and s[i] in sdic:
                    lastchar = stack.popleft()
                    sdic.pop(lastchar)
            stack.append(s[i])
            sdic[s[i]] = 1
            maxlength = max(maxlength, len(stack))

        return maxlength