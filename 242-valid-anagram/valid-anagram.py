class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds ={}
        dt = {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            ds[s[i]] = ds.get( s[i] , 0 ) + 1
            dt[t[i]] = dt.get( t[i] , 0 ) + 1
        for i,v in ds.items():
            if i not in dt or dt[i] != v :
                return False
        return True