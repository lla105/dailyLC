class DetectSquares:

    def __init__(self):
        self.d = {}

    def add(self, point: List[int]) -> None:
        x,y = point
        self.d[ (x,y) ] = self.d.get((x,y),0) + 1 

    def count(self, point: List[int]) -> int:
        count = 0
        x1,y1 = point
        for i,v in self.d.items():
            x2,y2 = i
            freq = v
            xdist = abs(x2-x1)
            ydist = abs(y2-y1)
            if xdist==ydist and xdist>0:
                corner3 = (x2,y1)
                corner4 = (x1,y2)
                if corner3 in self.d and corner4 in self.d:
                    count += freq * self.d[corner3] * self.d[corner4]
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)