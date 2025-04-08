class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        output = 0
        for i in range(len(height)):
            cur_h = height[i]
            while stack and height[stack[-1]] < cur_h :
                bottom = stack.pop()
                if not stack:
                    break
                min_h = min(cur_h , height[stack[-1]] ) - height[bottom]
                w = i - stack[-1] -1 
                output += min_h*w
            stack.append( i )
        return output