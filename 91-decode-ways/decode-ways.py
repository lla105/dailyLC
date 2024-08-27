class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string or starting with '0' can't be decoded
        if not s or s[0] == '0':
            return 0
        if len(s)==2 and int(s)>26:
            if s[-1]!='0':
                return 1
            else:
                return 0
        # Initialize dp array
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string has one way to be decoded
        dp[1] = 1  # A valid single character string has one way to be decoded
        print(dp)
        for i in range(2, n + 1):
            j = i-1
            print('====== ', s[j] )
            if (s[j]=='0' ) :
                if 10<=int(s[j-1:j+1])<=26:
                    dp[i] = dp[i-2]
                
            elif ( int(s[j-1:j+1]) >26):
                dp[i] = dp[i-1]
            elif s[j]!='0':
                if s[j-1]!='0': # prev # is not 0, like 21, 11
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                print( ' ELSE !!!')
            print(dp)
        return dp[n]
