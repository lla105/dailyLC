class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdic = Counter(p)
        sdic = {}
        result = []
        sString = deque()
        for i in range(len(s)):
            sdic[s[i]] = sdic.get(s[i] , 0) + 1
            sString.append(s[i])
            if i<len(p)-1:
                continue
            isAnagram = True
            for pi,pv in pdic.items():
                if pi in sdic and pv==sdic.get(pi):
                    pass
                else:
                    isAnagram = False
                    continue
            if isAnagram :
                result.append(i-len(p)+1)
                
            lastchar = s[i-len(p)+1]
            # if sdic.get(lastchar):
            #     print(lastchar, ' is good')
            # else:
            #     print(lastchar, ' is None')
            # print(i, ").     ", sdic)

            if sdic.get(lastchar) == 1:
                sdic.pop(lastchar)
            elif sdic.get(lastchar) >1:
                sdic[lastchar] -= 1
        return result