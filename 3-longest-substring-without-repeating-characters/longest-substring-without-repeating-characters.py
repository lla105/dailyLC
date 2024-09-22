class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        q = deque()
        # l = 0
        # r = 0
        seen = set()
        result = 0
        for i in range(len(s)):
            while s[i] in seen:
                # print(' >> ' , s[i] , ' is in s')
                num = q.popleft()
                seen.remove(num)
            seen.add( s[i] ) # a
            q.append( s[i] ) # a
            result = max(result, len(q))
        return result
