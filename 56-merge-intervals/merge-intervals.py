class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted( intervals, lambda=x x:x[0])
        intervals = sorted(intervals)
        stack = []

        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])
            elif stack[-1][1] >= intervals[i][0] :
                # print( stack[-1] , ' vs ', intervals[i])
                stack[-1][0] = min(stack[-1][0] , intervals[i][0])
                stack[-1][1] = max(stack[-1][1] , intervals[i][1])
            else:
                stack.append(intervals[i])

        return stack