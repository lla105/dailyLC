from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdic = Counter(p)
        sdic = Counter(s[:len(p)])
        result = []
        
        if pdic == sdic:
            result.append(0)
        
        for i in range(len(p), len(s)):
            sdic[s[i]] += 1
            sdic[s[i - len(p)]] -= 1
            
            if sdic[s[i - len(p)]] == 0:
                del sdic[s[i - len(p)]]
                
            if pdic == sdic:
                result.append(i - len(p) + 1)
        
        return result
