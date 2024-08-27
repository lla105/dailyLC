class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            j = i-1
            twodigits = int(s[j-1:j+1])
            # if s[j]=='0' :
            #     if twodigits==10 or twodigits==20:
            #         dp[i] = dp[i-2]
            #     else:
            #         return 0

            # else:
            #     if twodigits>=10 and twodigits<=26:
            #         dp[i] = dp[i-1] + dp[i-2]
            #     else:
            #         dp[i] = dp[i-1]
            if s[j]!='0' :
                dp[i] += dp[i-1]
            if twodigits >= 10 and twodigits <= 26:
                dp[i] += dp[i-2]
            # print(dp)
        return dp[-1]
