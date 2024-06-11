class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1,n+1):
            print(i,") ", s[i-1])
            for word in wordDict:
                print('<<<<<', s[i-len(word):i] , ' vs ', word)
                if i>=len(word):
                    print('    3) length good')
                    if s[i-len(word):i]==word:
                        print('     4) word equal: ')
                        print('        ', i,'-', len(word),'=',i-len(word))
                        if dp[i-len(word)] is True:
                            dp[i] = dp[i-len(word)]
        print(dp)
        return dp[-1]