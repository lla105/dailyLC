class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        self.pdic = Counter(p)
        self.sdic = Counter(s[0:len(p)])
        # del self.sdic['c']
        self.result = []
        if self.pdic == self.sdic:
            self.result.append(0)
        for i in range(len(p), len(s)):
            lastchar = s[i-len(p)]
            # print(i)
            # print(' last char : ' , lastchar)
            if self.sdic.get(lastchar) > 1:
                self.sdic[lastchar] -= 1
            else:
                del self.sdic[s[i-len(p)]]


            self.sdic[s[i]] = self.sdic.get(s[i] , 0) + 1
            if self.pdic == self.sdic:
                # print( ' MATCH ')
                self.result.append(i-len(p)+1 )
        return self.result

