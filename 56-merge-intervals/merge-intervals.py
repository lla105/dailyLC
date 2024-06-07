class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals , key=lambda x:x[0])
        answerlist = []
        for i in range(len(intervals)):
            curinterval = intervals[i]
            curstart = intervals[i][0]
            curend = intervals[i][1]
            if len(answerlist)==0:
                answerlist.append(curinterval)
            elif answerlist[-1][1] >= curstart:
                answerlist[-1][1] = max(answerlist[-1][1] , curend)
                answerlist[-1][0] = min(answerlist[-1][0] , curstart)
            else: 
                answerlist.append(curinterval)
                
            
        return answerlist