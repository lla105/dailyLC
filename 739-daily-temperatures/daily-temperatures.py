class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        result = [0] * (len(t))
        for i in range(len(t)):
            if not stack:
                stack.append( (t[i], i) )
                continue
            while stack and stack[-1][0] < t[i]:
                result[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append( (t[i], i) )
        return result