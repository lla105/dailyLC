class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []
        max_size = 0
        for i in range(len(rectangles)):
            num1 = rectangles[i][0]
            num2 = rectangles[i][1]
            arr.append( min(num1,num2) )
            max_size = max( max_size, min(num1,num2))
        print(' arr : ', arr)
        output = 0
        for num in arr :
            if num == max_size :
                output += 1
        return output
        # d = {} # format : { value:freq }
        # for num in arr :
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1
        # output = 0
        # for i,v in d.items():
        #     output = max( output, v )
        # return output