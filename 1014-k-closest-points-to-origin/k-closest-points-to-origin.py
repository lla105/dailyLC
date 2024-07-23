import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def geteuc(points):
            # points = [ (x,y) ]
            x = points[0]
            y = points[1]
            xx = x*x
            yy = y*y
            tempsum = xx+yy
            return math.sqrt(tempsum)
        
        shortest = float('inf')
        result = []
        arr = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            curdist = geteuc(points[i])
            arr.append( (curdist, (x,y)))
        print('arr > ', arr)
        arr = sorted(arr, key=lambda x:x[0])
        print('arr > ', arr)
        
        for i in range(len(arr)):
            if k>0:
                result.append(arr[i][1])
            else:
                return result
            k-=1
        return result