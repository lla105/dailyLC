class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        q = deque()
        output = 0
        for i in range(len(s)):
            if s[i] in sset :
                while q and q[0] != s[i]:
                    num = q.popleft()
                    sset.remove(num)
                if q:
                    num = q.popleft()
                    sset.remove(num)
            sset.add(s[i])
            q.append(s[i])
            output = max(output, len(q))
        return output
