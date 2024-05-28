class Solution:
    def insert(self, intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i<len(intervals) and intervals[i][1]<newIntervals[0]:
            result.append(intervals[i])
            i+=1
        
        # the remaining intervals[i][1] are > newIntervals[0]
        while i<len(intervals) and newIntervals[1]>=intervals[i][0]:
            newIntervals[0] = min(newIntervals[0] , intervals[i][0])
            newIntervals[1] = max(newIntervals[1] , intervals[i][1])
            i+=1
    
        result.append(newIntervals)

        while i<len(intervals):
            result.append(intervals[i])
            i+=1

        return result