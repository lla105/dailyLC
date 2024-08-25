class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # self.result = False
        # def bf( curList ) : 
        #     # print('   looking for : ', s[len(curList): ] , curList)
        #     if len(curList) > len(s):
        #         return
        #     if len(curList) == len(s):
        #         self.result = True

        #     for i in range(len(wordDict)):
        #         if wordDict[i] == s[len(curList) : len(curList)+len(wordDict[i])]:
        #             bf( curList+str(wordDict[i] ))
        # bf('')
        # return self.result
        dp = [False ] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(len(wordDict)):
                word = wordDict[j]
                if word==s[i:i+len(word)]:
                    dp[i+len(word)] = True
        print(dp)
        return dp[-1]