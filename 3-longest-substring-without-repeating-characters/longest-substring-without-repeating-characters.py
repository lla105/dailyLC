class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        output = 0
        l = 0
        for r in range(len(s)):
            if r==0:
                seen[s[r]] = 1
                output +=1
                continue
            while  s[r] in seen :
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l+=1
            output = max(output, r-l+1 )
            seen[s[r]] = seen.get(s[r], 0 ) + 1
            # print(s[l:r+1], seen)

        return output