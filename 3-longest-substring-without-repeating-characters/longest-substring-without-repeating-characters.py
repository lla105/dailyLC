class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        longest = 0
        ss = []
        for i in range(len(s)):
            char = s[i]
            while char in ss:
                ss.pop(0)
            ss.append(char)
            # print(ss)
            longest = max(longest, len(ss))

        return longest