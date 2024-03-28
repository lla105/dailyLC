class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        templist = []
        def traverse(s,l,r):
            count = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        for i in range(len(s)):
            result += traverse(s,i,i) + traverse(s,i,i+1)
        return result


        