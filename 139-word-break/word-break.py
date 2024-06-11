class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            print(i)
            for word in wordDict:
                print(s[i-len(word) : i])
                if i>=len(word):
                    if s[i-len(word) : i] == word:
                        print(' num is good!!!')
                        if dp[i-len(word)] :
                            dp[i] = dp[i-len(word)]

        return dp[-1]