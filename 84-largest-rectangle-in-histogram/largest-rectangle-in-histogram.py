class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==1:
            return heights[-1]
        stack = []
        maxarea = 0
        for i in range(len(heights)):
            startindex = i
            if stack and heights[i] < stack[-1][0]:
                while stack and heights[i] < stack[-1][0]:
                    w = i - stack[-1][1] 
                    h = stack[-1][0]
                    curarea = w*h
                    maxarea = max(maxarea, curarea)
                    startindex = stack[-1][1]
                    stack.pop()
                stack.append( (heights[i], startindex) )
            else:
                stack.append( (heights[i], startindex) )
            # print('cur stack: ', stack)

        print('stack after 1st round: ', stack)
        for i in range(len(stack)-1, 0, -1):
            # print(stack[i][0] , stack[i][1])
            w = len(heights)-stack[i][1]
            h = stack[i][0]
            temparea = w*h
            # print(i,")   ", w,"*",h,"=",temparea)
            maxarea = max(temparea, maxarea)
        w = len(heights)
        h = stack[0][0]
        temparea = w*h
        print("x)   ", w,"*",h,"=",temparea)

        maxarea = max(temparea, maxarea)

        
        return maxarea