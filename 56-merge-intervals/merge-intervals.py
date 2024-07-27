class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        for i in range(len(intervals)):
            if not result:
                result.append(intervals[i])
                continue
            if result[-1][1] >= intervals[i][0]:
                result[-1][0] = min(result[-1][0] , intervals[i][0])
                result[-1][1] = max(result[-1][1] , intervals[i][1])
            else:
                result.append(intervals[i])
        return result