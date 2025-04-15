class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        def get_dist(x,y):
            xsq = abs(x*x)
            ysq = abs(y*y)
            temp = sqrt( xsq+ysq )
            # d[temp] = (x,y)
            if temp in d:
                d[temp].append( (x,y) )
            else:
                d[temp] = [ (x,y) ]
            return temp
        arr = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            temp = get_dist(x,y)
            # print('>>>', temp)
            arr.append(temp)
        heapq.heapify(arr)
        count = 0
        output = []
        print('heap : ', arr)
        while count < k:
            rm_num = heapq.heappop(arr)
            print('rm_num: ', rm_num)
            array = d[rm_num]
            for item in array:
                output.append( item )
                count+=1
            # print(rm_num)
        return output