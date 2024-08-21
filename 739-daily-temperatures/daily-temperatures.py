class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                oldt, oldi = stack.pop()
                result[oldi] = i-oldi

            stack.append( (t,i) )
        return result
