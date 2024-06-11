class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        print(dp)

        for i in range( len(s)-1 , -1 , -1):
            for word in wordDict:
                print(len(s) , i , len(word), word)
                if (len(s)-i >= len(word)) :
                    print(' len is good. word: ', s[i:i+len(word)])
                    if s[i:i+len(word)] == word:
                        # print('.  match!!! : ', word, ' vs ', s[len(s):i+1])
                        dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break
                    
        return dp[0]