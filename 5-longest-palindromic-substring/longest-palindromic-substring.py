class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxsubstring = ''
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                cursubstring = s[l:r+1]
                if len(cursubstring) >= len(maxsubstring):
                    maxsubstring = cursubstring
                
                l-=1
                r+=1
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                cursubstring = s[l:r+1]
                if len(cursubstring) >= len(maxsubstring):
                    maxsubstring = cursubstring
                
                l-=1
                r+=1

        return maxsubstring