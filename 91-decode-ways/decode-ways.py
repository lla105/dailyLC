class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: If the string starts with '0', it's not decodable
        if s[0] == '0':
            return 0
        
        # Initialize the dp array to store the number of ways to decode up to each index
        dp = [0] * len(s)
        
        # Base case: There's 1 way to decode the first character if it's valid (not '0')
        dp[0] = 1
        
        # Handle the second character based on its value
        if len(s) > 1:
            # If the first two digits form a valid number <= 26
            if 10 <= int(s[0:2]) <= 26:
                # If the second digit is not '0', we have two possible decodings
                if s[1] != '0':
                    dp[1] = 2
                # If the second digit is '0', we can only decode the two digits as a pair
                else:
                    dp[1] = 1
            # If the two digits form an invalid number (> 26 or contains a '0' in a wrong position)
            else:
                # If the second digit is '0', the string is invalid
                if s[1] == '0':
                    return 0
                # Otherwise, there's only one way to decode the second character
                else:
                    dp[1] = 1
        
        # Iterate through the rest of the string, applying the decoding rules
        for i in range(2, len(s)):
            # If the current digit is '0', it must be part of a valid two-digit number (10 or 20)
            if s[i] == '0':
                # Check if the previous digit forms a valid two-digit number with the current '0'
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                # If not, it's an invalid encoding
                else:
                    return 0
            # If the current digit is between '1' and '9'
            else:
                # If the previous two digits form a valid number (10 to 26), add ways from dp[i-2]
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                # If the two digits don't form a valid number, just carry forward the dp[i-1] value
                else:
                    dp[i] = dp[i-1]
        
        # The result is stored in the last position of the dp array
        return dp[-1]
