class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            j = i - 1

            # Check if the current character is '0'
            if s[j] == '0':
                if 10 <= int(s[j-1:j+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    return 0  # Invalid encoding when '0' is not part of "10" or "20"
            else:
                # If the two-digit number is valid, consider both dp[i-1] and dp[i-2]
                if 10 <= int(s[j-1:j+1]) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

        return dp[n]
