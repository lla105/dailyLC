class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [4,5], [5,7],[8,9]
        # newiunbteraval: [5,11]
        # [4,11]
        result = []
        i = 0
        newint = newInterval
        while i<len(intervals) and intervals[i][0]<newint[0] and intervals[i][1]<newint[0]:
            result.append(intervals[i])
            i+=1
        tempint = newint
        while i<len(intervals) and intervals[i][0] <= newint[1]:
            # print(intervals[i][0])
            tempint[0] = min(intervals[i][0] , newint[0])
            tempint[1] = max(intervals[i][1] , newint[1])
            i+=1
        result.append(tempint)
        # print('2.   ', result)
        while i<len(intervals) and intervals[i]:
            result.append(intervals[i])
            i+=1
        return result
        