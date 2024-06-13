class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # format = [ (temp, index) , ...]
        t = temperatures
        result = [0] * len(t)
        for i in range(len(t)):
            if not stack:
                stack.append( (t[i] , i) )
            else:
                # print(stack)
                while len(stack)>0 and stack[-1][0] < t[i] :
                    result[stack[-1][1]] = (i-stack[-1][1])
                    stack.pop()
                    # print(' while loop end')
                stack.append( (t[i] , i) )
        
        return result
