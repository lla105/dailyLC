class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False
            
            s1count = Counter(s1)
            window = Counter(s2[:len(s1)])

            matches = 0
            for char in s1count:
                if s1count[char] == window[char]:
                    matches += 1

            # Sliding window logic
            for i in range(len(s1), len(s2)):
                if matches == len(s1count):
                    return True

                # Add new character to the window
                char_in = s2[i]
                window[char_in] += 1
                if char_in in s1count:
                    if window[char_in] == s1count[char_in]:
                        matches += 1
                    elif window[char_in] == s1count[char_in] + 1:
                        matches -= 1

                # Remove the old character from the window
                char_out = s2[i - len(s1)]
                if window[char_out] == s1count[char_out]:
                    matches -= 1
                window[char_out] -= 1
                if char_out in s1count and window[char_out] == s1count[char_out]:
                    matches += 1

            return matches == len(s1count)