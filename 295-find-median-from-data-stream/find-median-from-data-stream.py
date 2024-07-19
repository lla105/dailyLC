class MedianFinder:

    def __init__(self):
        self.stack = []

    def addNum(self, num: int) -> None:
        if not self.stack:
            self.stack.append(num)
        else:
            l, r = 0, len(self.stack)
            while l < r:
                mid = (l + r) // 2
                if self.stack[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            self.stack.insert(l, num)
            
        # print(self.stack)

    def findMedian(self) -> float:
        if len(self.stack)%2 == 0 : # is even
            v1 = self.stack[len(self.stack)//2]
            v2 = self.stack[ (len(self.stack)//2) -1 ]
            return (v1+v2)/2
        else:
            return self.stack[ len(self.stack)//2 ]
        return 99
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()