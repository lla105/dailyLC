class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False ] * (len(s) + 1)
        dp[0] = True
        # dp[1:len(s)] = s[0:-1]

        for i in range(len(s)):
            if dp[i] :
                for word in wordDict:
                    # print(i,s[i: i+len(word)], word)
                    if s[i : i+len(word) ] == word :
                        dp[i+len(word)] = True
                # print(dp)

        return dp[-1]

