class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i in range(len(heights)):
            h = heights[i]
            if not stack:
                stack.append( (h,i) )
                continue
            if stack[-1][0] <= h:
                stack.append( (h,i) )
            else:
                savei = i
                while stack and stack[-1][0] > h:
                    oldh, oldi = stack.pop()
                    curw = i-oldi
                    curh = oldh
                    largest = max(largest, curh*curw)
                    savei = oldi
                stack.append( (h,savei) )
        newstack = []
        for i in range(len(stack)):
            if not newstack:
                newstack.append( stack[i] )
            else:
                if newstack[-1][0] == stack[i][0]:
                    continue
                else:
                    newstack.append( stack[i] )
        for i in range(len( stack )):
            if i==0:
                curw = len(heights)
                curh = stack[i][0]
            else:
                curw = len(heights) - stack[i][1]
                curh = stack[i][0]
            largest = max(largest, curw*curh)
                
        return largest