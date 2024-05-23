class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = Counter(s)
        t = Counter(t)

        print(s)
        print(t)
        for i,v in s.items():
            if s[i] != t[i]:
                return False
        return True