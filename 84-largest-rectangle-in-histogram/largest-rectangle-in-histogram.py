class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] 
        #format is [ [index1, height1] , [index2, height2] , ..... ]
        # most recent height = stack[-1][1]
        # most recent index = stakc[-1][0]

        for i,h in enumerate(heights):
            start = i
            # if cur height < stack[-1] height, pop it and calculate, 
            while len(stack)>0 and h<stack[-1][1]:
                oldi, oldh = stack.pop()
                area = oldh * (i - oldi)
                maxArea = max(area, maxArea)
                start = oldi
            stack.append( (start,h) )
            # compare with max height.

        for i,h in stack:
            print(f'{i}, {h}')
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea