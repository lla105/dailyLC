class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Create a new string that is the reverse of s
        rev_s = s[::-1]
        # Concatenate s with a separator and its reverse
        new_s = s + "#" + rev_s
        
        # Build the KMP table
        lps = [0] * len(new_s)
        j = 0  # Length of the previous longest prefix suffix
        
        for i in range(1, len(new_s)):
            while (j > 0 and new_s[i] != new_s[j]):
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
                lps[i] = j
        
        # The length of the longest palindromic prefix
        longest_palindromic_prefix_len = lps[-1]
        
        # Append the necessary characters to the beginning of s
        return rev_s[:len(s) - longest_palindromic_prefix_len] + s