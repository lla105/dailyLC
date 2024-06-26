class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            prevDigit = int(s[i-1])
            prev2Digits = int(s[i-2:i])

            if prevDigit!=0:
                dp[i] += dp[i-1]
            if 10<=prev2Digits<=26:
                dp[i] += dp[i-2]


        print(dp)
        return dp[-1]