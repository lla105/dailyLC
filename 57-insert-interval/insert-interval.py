class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        # intervals = [3,5],[12,13]
        # newinterval = [4,10] or [2,10]   
        tempinterval = newInterval     
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            tempinterval[0] = min(tempinterval[0], intervals[i][0])
            tempinterval[1] = max(tempinterval[1], intervals[i][1])
            i+=1
        result.append(tempinterval)
        print('result : ', result)

        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        print('result 2 : ', result)
        

        return result