class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)):
            curheight = heights[i]
            startindex = i
            while len(stack)>0 and stack[-1][0] > curheight:
                # print('entering loop with: ', i,':',curheight)
                tempwidth = i - stack[-1][1]
                temparea = tempwidth * stack[-1][0]
                maxarea = max(maxarea, temparea)
                startindex = stack[-1][1]
                stack.pop()

            stack.append( (curheight, startindex))
            # print('stack: ', stack)
            # print('maxarea so far: ', maxarea)
        maxstacklength = len(stack) 

        # for i in range(len(stack)):
        #     tempwidth = maxstacklength - i
        #     temparea = tempwidth * stack[i][0]
        #     maxarea = max(maxarea, temparea)

        for i in range(len(stack)):
            curheight = stack[i][0]
            curindex = stack[i][1]
            temparea = curheight * (len(heights) - curindex)
            maxarea = max(temparea, maxarea)
        print()
        print('maxarea final : ', maxarea)
        return maxarea