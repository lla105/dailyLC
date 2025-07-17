class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Transform string with separators
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        center = 0
        right = 0

        max_len = 0
        max_center = 0

        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around center i
            a = i + p[i] + 1
            b = i - p[i] - 1
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary if needed
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Track max palindrome
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # Extract the actual palindrome from the original string
        start = (max_center - max_len) // 2
        return s[start:start + max_len]