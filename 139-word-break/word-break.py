class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False ] * ( len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i] : 
                continue
            for word in wordDict:
                if s[i:i+len(word)] == word :
                    dp[i+len(word)] = True
        return dp[-1]
        # dp = [ False ] * ( len(s) + 1 )
        # dp[0] = True
        # wordSet = set(wordDict)

        # def explore( index ) :
        #     if index == len(s):
        #         dp[index] = True
        #     if index >= len(s):
        #         print(' Over length ')
        #         return

        #     print(' >>>> explore (', index,'): ', s[index])
        #     dp[index] = True
        #     for word in wordDict:
        #         if s[index:index+len(word)] != word or not dp[i] :
        #             continue
        #         print('3)  word: ', word, ' vs ', s[index:index+len(word)])
        #         explore (index+len(word))

        # for i in range(len(s)):
        #     for word in wordDict:
        #         if i+len(word) >= len(s) or s[i:i+len(word)] != word or not dp[i]:
        #             continue
        #         print('1) match: ', s[i:i+len(word)])
        #         explore( i+len(word) )

        # return dp[-1]