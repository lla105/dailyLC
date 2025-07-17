class Solution:
    def longestPalindrome(self, s: str) -> str:
        def count_even_pal(idx):
            l = idx
            r = idx+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1 : r]
        def count_odd_pal(idx):
            l = idx
            r = idx
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1 : r]
        output = ""
        for i in range(len(s)):
            even_string = count_even_pal(i)
            odd_string = count_odd_pal(i)
            if len(even_string) > len(output):
                output = even_string
            if len(odd_string) > len(output):
                output = odd_string
        return output
# s = 12378321
# s = abba <- even case
# s = aba. <- odd case
