class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        wordset = set()

        for i in range(len(s)):
            word1 = s[i+1:]
            word2 = s[:i+1]
            word3 = word1
            wordset.add( word1 + word2 )

        if goal in wordset:
            return True
        else:
            return False