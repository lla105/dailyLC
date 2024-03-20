class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        lst = []
        # lst.append('a')
        # lst.append('b')
        # lst.append('c')
        # print(lst)
        # lst.pop(0)
        # print(lst)
        for i in range(len(s)):
            char = s[i]
            while char in lst:
                lst.pop(0)
            lst.append(char)
            longest = max(longest, len(lst))
        return longest
