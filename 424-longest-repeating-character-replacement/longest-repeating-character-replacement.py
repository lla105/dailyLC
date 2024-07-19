class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        highestfreq = 0 
        d = {}
        q = deque()
        for i in range(len(s)):
            d[s[i]] = d.get(s[i] , 0 ) + 1
            highestfreq = max(highestfreq , d[s[i]])
            if k > len(q) - highestfreq:
                q.append(s[i])
            else:
                d[s[i-len(q)]] -= 1
            # print(q)
        return len(q)
