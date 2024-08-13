class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [ False ] * (len(s)+1)
        dp[0] = True
        # print(dp)

        for i in range(len(dp)):
            if not dp[i]:
                continue
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = True
                    # print(dp)
                # print(s[i:i+len(word)])
        return dp[-1]