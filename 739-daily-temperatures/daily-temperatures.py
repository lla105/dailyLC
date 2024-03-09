class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        # where tempa must be > tempb
        # and tempa has structure : [ curtemp, curday/i ]
        t = temperatures
        length = len(t)
        # structure: s = [ tempa, tempb , ...]
        s = [] 
        result = [0] * length
        # for curtemp in t
        for curday, curtemp in enumerate(t):
            # print(f'{curday}, {curtemp}')
            # while .....
            while len(s)!=0 and curtemp>s[-1][0] :
                previousday = s[-1][1]
                difference = curday - previousday
                result[previousday] = difference
                s.pop(-1)
            s.append( [curtemp, curday])
        return result
        # if curtemp > s[-1]
        # pop tempb, and update dayb with answer by: curday - dayb

        # if stack is empty, means constantly getting hotter
