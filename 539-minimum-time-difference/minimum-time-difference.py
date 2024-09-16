class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(hhmm) :
            hour = int(hhmm[0:2])
            minute = int(hhmm[3:5])
            # print(hour, minute)
            totaltime = (hour*60) + minute
            return totaltime
        timelist = []
        timeset = set()
        for tp in timePoints:
            if tp in timeset:
                return 0
            timeset.add(tp)
            timelist.append(convert(tp))
            # print(temp)
        timelist = sorted(timelist)
        result = float('inf')
        for i in range(len(timelist)):
            if i == 0 and len(timelist)>1:
                timediff = abs(timelist[0] - timelist[-1])
                result = min(result, timediff, 1440-timediff )
                continue
            timediff = abs( timelist[i] - timelist[i-1] )
            result = min(result, timediff, 1440-timediff )
        return result