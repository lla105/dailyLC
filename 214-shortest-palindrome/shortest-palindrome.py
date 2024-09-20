class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Create the reversed string
        rev_s = s[::-1]
        # Concatenate s + '#' + rev_s to avoid overlap issues
        combined = s + '#' + rev_s
        
        # KMP-style table to find the longest prefix palindrome
        lps = [0] * len(combined)
        
        # Build the KMP table (longest prefix suffix array)
        for i in range(1, len(combined)):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        # lps[-1] gives us the longest palindrome starting from index 0
        longest_palindrome_len = lps[-1]
        
        # The part we need to add is the remaining part after the palindrome
        add_on = rev_s[:len(s) - longest_palindrome_len]
        
        return add_on + s
