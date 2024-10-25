class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxlen = 0
        maxstring = ''
        whatj= 0
        for i in range(len(s)):
            #even 
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen < len(s[l:r+1]) :
                    maxlen = len(s[l:r+1])
                    maxstring = s[l:r+1]
                l-=1
                r+=1
            
            #odd
            l=i
            r=i
            print()
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen < len(s[l:r+1]):
                    maxlen = len(s[l:r+1])
                    maxstring = s[l:r+1]
                l-=1
                r+=1
        print("asdfasf")
        return maxstring
