class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        pdic = {}
        for i in range(len(s)):
            sdic[s[i]] = sdic.get(s[i], 0) + 1
            pdic['a'] = 2+2
        print(sdic)
        tdic = {}
        for i in range(len(t)):
            tdic[t[i]] = tdic.get(t[i] , 0) + 1
        print(tdic)

        # print(tdic == sdic)
        return tdic==sdic

        return True