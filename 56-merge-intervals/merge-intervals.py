class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        resultlist = []
        intervals = sorted(intervals, key=lambda x:x[0])
        print(intervals)
        for i in range(len(intervals)):
            if not resultlist:
                resultlist.append(intervals[i])
                continue
            if resultlist[-1][1] >= intervals[i][0]:
                resultlist[-1][0] = min(resultlist[-1][0] , intervals[i][0])
                resultlist[-1][1] = max(resultlist[-1][1] , intervals[i][1])
            else:
                resultlist.append(intervals[i])

        return resultlist