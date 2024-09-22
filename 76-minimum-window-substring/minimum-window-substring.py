class Solution:
    def minWindow(self, s: str, t: str) -> str:
        self.match = 0
        q = deque()
        d1 = {}
        d2 = {}
        result = float('inf')
        left = 0  # Left pointer for the sliding window
        min_len = float('inf')
        start_idx = 0  # To track the start index of the minimum window

        # Populate the frequency map for `t`
        for char in t:
            d1[char] = d1.get(char, 0) + 1
        
        required = len(d1)  # Number of unique characters we need to match
        formed = 0  # Number of unique characters we have matched

        # Dictionary to count characters in the current window
        window_counts = {}

        # Right pointer for the sliding window
        for right in range(len(s)):
            char = s[right]
            
            # Add the character to the window
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character's count matches the required count, increment `formed`
            if char in d1 and window_counts[char] == d1[char]:
                formed += 1

            # When we have a valid window, try to minimize it
            while left <= right and formed == required:
                char = s[left]

                # Update the result if we found a smaller valid window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start_idx = left

                # Remove the leftmost character from the window
                window_counts[char] -= 1
                if char in d1 and window_counts[char] < d1[char]:
                    formed -= 1
                
                left += 1  # Move the left pointer

        return "" if min_len == float('inf') else s[start_idx:start_idx + min_len]
