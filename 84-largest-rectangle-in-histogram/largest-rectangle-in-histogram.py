class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i in range(len(heights)):
            h = heights[i]
            startindex = i

            while len(stack)>0 and stack[-1][0]>h:
                oldh, oldi = stack.pop()
                temparea = oldh * (i-oldi)
                maxarea = max(maxarea, temparea)
                startindex = oldi

            stack.append( (h,startindex) )

        print(">>>", stack)
        for i in range(len(stack)):
            currh = stack[i][0]
            curri = stack[i][1]
            # print(f'{currh} * {len(stack)} - {curri}')
            temparea = currh * (len(heights) - curri )
            maxarea = max(temparea, maxarea)

        return maxarea