class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        q = deque()
        max_freq = 0
        max_len = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0 ) + 1
            max_freq = max(max_freq, d[s[i]] )
            q.append(s[i])
            if k < len(q) - max_freq:
                leftchar = q.popleft()
                d[leftchar] -= 1
            max_len = max(max_len, len(q))
        return max_len
        