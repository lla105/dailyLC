class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # print(result)
        temp = newInterval

        while i<len(intervals) and intervals[i][0] <= temp[1] :
            temp[0] = min(temp[0], intervals[i][0])
            temp[1] = max(temp[1], intervals[i][1])
            i+=1
        result.append(temp)
        # print(result)
        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        return result