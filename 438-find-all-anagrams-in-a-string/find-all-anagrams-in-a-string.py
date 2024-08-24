class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        scount = Counter(s[:len(p)])

        result = []
        l = 0
        if scount == pcount:
            result.append(0)
            
        for r in range(len(p) , len(s)):
            scount[s[r]] = scount.get(s[r],0) + 1
            scount[s[l]] -= 1

            if scount[s[l]] == 0:
                scount.pop(s[l])
            l+=1
            if scount == pcount : 
                result.append(l)

        return result
