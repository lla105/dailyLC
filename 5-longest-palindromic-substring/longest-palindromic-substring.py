class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        def pal_len( idx , is_even ) :
            if is_even:
                l = idx
            else:
                l = idx-1
            r = idx+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            return s[l:r+1]
        for i in range(len(s)):
            even = pal_len(i,is_even=True)
            odd = pal_len(i,is_even=False)
            if len(even) > len(output) :
                output = even
            if len(odd) > len(output) :
                output = odd
        return output

#s1=aba
#s2=abba

# s= babad
# b
#   b
#   ba
# a
#   bab 
#   ab
# s = cbbd
# c
# b
#   cbb
#   bb
#       cbbd NOPE
