class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stack = deque()
        ss = set()
        count = 0
        answer = 0
        for i in range(len(s)):
            # if s[i] not in ss and s[i] not in stack:
            #     stack.append(s[i])
            #     ss.add(s[i])
            #     count+=1

            # else:
            while s[i] in ss:
                removed = stack.popleft()
                ss.remove(removed)
                count -= 1
            stack.append(s[i])
            ss.add(s[i])
            count+=1
            answer = max(answer, count)

        return answer
                