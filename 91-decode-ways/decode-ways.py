class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1
        #nums= [ ,1,2,3,0]
        # dp = [1,1,0,0,0]

        # if cur num is not 0, i-1 + i-2
        for i in range(2, len(dp)):
            # print(s)
            # dp[i] = 99
            prev1Digit = int(s[i-1])
            prev2Digits = int(s[i-2:i])

            if prev1Digit!=0:
                dp[i] += dp[i-1]
            if 10<=prev2Digits<=26:
                dp[i] += dp[i-2]


        print(dp)
        return dp[-1]