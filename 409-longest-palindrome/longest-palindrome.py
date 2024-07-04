class Solution:
    def longestPalindrome(self, s: str) -> int:
        scount = Counter(s)
        pairs = 0
        hasOdd= False
        for i,v in scount.items():
            pairs += (v//2)*2
            if v%2!=0:
                hasOdd = True

        if hasOdd:
            return pairs+1
        else:
            return pairs