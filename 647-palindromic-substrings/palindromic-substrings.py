class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0

        def isPal(l,r):
            count = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            answer += isPal(i,i) + isPal(i,i+1)

        return answer