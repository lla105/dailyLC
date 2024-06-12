class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answerlist = []
        intervals = sorted(intervals, key=lambda x:x[0])
        
        for i in range(len(intervals)):
            curinterval = intervals[i]
            if not answerlist:
                answerlist.append(curinterval)
            elif answerlist[-1][1] >= curinterval[0]:
                answerlist[-1][0] = min(answerlist[-1][0] , curinterval[0])
                answerlist[-1][1] = max(answerlist[-1][1] , curinterval[1])
            else:
                answerlist.append(curinterval)
        print(answerlist)
        return answerlist