class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        length = len(t)

        result = [0]*length
        #monotonic stack structure : [ {tempa:daya} , {tempb:dayb} , ....]
        s = [ ]

        for curday, curtemp in enumerate(t):
            # print(f'{curday} : {curtemp}')
            if curday == 0:
                # s.append({curday:curtemp})
                s.append([curday, curtemp])
            while len(s)!=0 and curtemp>s[-1][1]:
                daydiff = abs(s[-1][0] - curday)
                result[s[-1][0]] = daydiff
                s.pop()
            s.append( [curday, curtemp])

        # print(f'{s} and {result}')
        return result