class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [ '' ]
        for i in range(len(s)):
            # print( i)
            #odd palindromes
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # print(len(s[l:r+1]) ,  ' vs ', len(longest[-1]))
                if len(s[l:r+1]) > len(longest[-1]) :
                    longest.append(s[l:r+1])
                    # print(s[l:r+1], l, r)

                l-=1
                r+=1

            #even palindromes
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) > len(longest[-1]) :
                    longest.append(s[l:r+1])
                    # print(s[l:r+1], l, r)

                l-=1
                r+=1
        # print(longest)

        return longest[-1]