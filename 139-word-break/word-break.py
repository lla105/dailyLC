class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False ] * (len(s)+1)
        dp[0] = True
        print(dp)
        
        for i in range(len(s)):
            if dp[i]:  # Only proceed if the substring up to i can be segmented
                for word in wordDict:
                    end_index = i + len(word)
                    if end_index <= len(s) and s[i:end_index] == word:
                        dp[end_index] = True
        
        return dp[len(s)]
        print(dp)
        return dp[-1]