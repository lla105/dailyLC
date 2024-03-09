class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        length = len(t)
        print(t)
        s = [] # format [ [temp,day] , [temp,day] ]
        result = [0]*length
        # { index : amount of days}
        # t.pop(0) <-- pops from the head

        # monotonic stack = [ tempa, tempb, tempc ...]
        # where tempa, tempb, tempc is of format: { temp : i }
        #for loop from front to back
        for curday, curtemp in enumerate(t):
            # print(f'{curday}, {curtemp}')
            # print(f'curday) : {curday}')
            while len(s)>0 and curtemp>s[-1][0] :
                prevday = s[-1][1]
                diffday = curday - prevday
                result[prevday] = diffday 
                s.pop(-1)
            s.append([curtemp, curday])

        return result
        # in mono stack, if i'm adding tempd, 
        # tempd must be SMALLER than everything preceeding
        # if tempd is BIGGER than previous, 
        # pop previous while tempd>previous
        # if tempd is SMALLER than previous,
        # simply stack on top of mono stack

        # the remaining ones in the stack are all 0s ?