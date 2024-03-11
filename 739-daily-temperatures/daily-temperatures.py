class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        length = len(t)

        result = [0]*length # format is : [ int, int , int ]
        stack = [ ] # format is : [ [tempa,daya] , [tempb,dayb] , ..]

        for curday, curtemp in enumerate(t):
            while len(stack)!=0 and curtemp>stack[-1][0]  :
                daydiff = abs(curday - stack[-1][1])
                print(f'>>> {stack[-1][1]}')
                result[stack[-1][1]] = daydiff
                stack.pop(-1)

            stack.append([curtemp,curday])
            
        return result