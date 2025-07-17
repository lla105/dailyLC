class Solution:
    def countSubstrings(self, s: str) -> int:
        self.output = 0

        def find_palin(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                # print(s[l:r+1])
                l-=1
                r+=1
                self.output+=1
            return (l+1,r-1)
        for i in range( len(s) ):
            # self.output+=1
            # print('>>', s[i])
            find_palin(i,i) # odd
            find_palin(i,i+1) # even
        return self.output