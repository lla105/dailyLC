class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string or starting with '0' can't be decoded
        if not s or s[0] == '0':
            return 0
        
        # Initialize dp array
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string has one way to be decoded
        dp[1] = 1  # A valid single character string has one way to be decoded

        # Fill the dp array
        for i in range(2, n + 1):
            # Single digit decode is valid (1-9)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Two digit decode is valid (10-26)
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        # The answer is the number of ways to decode the entire string
        return dp[n]
