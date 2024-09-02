from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculate the remainder of k after full rounds
        temp = k % sum(chalk)
        
        # Loop over the students to find the one who will run out of chalk
        for i, c in enumerate(chalk):
            if temp < c:
                return i
            temp -= c
        
        # The loop should always return a result before completing, but just in case:
        return -1  # This case should never be hit
