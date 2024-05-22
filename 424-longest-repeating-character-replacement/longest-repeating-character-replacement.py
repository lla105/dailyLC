class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestChar = 0
        substringLength = 0
        d = {}

        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0 ) + 1
            longestChar = max(longestChar, d[s[i]] )
            if k > substringLength - longestChar:
                substringLength += 1
            else :
                d[s[i - substringLength]] -= 1 
        return substringLength