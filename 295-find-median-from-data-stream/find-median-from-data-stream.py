class MedianFinder:

    def __init__(self):
        self.stack = []

    def addNum(self, num: int) -> None:
        if not self.stack:
            self.stack.append(num)
        else:
            # Binary search to find the correct insertion point
            l, r = 0, len(self.stack)
            while l < r:
                mid = (l + r) // 2
                if self.stack[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            self.stack.insert(l, num)
        # bisect.insort_left(self.stack, num)
        # if not self.stack:
        #     self.stack.append(num)
        # else:
        #     l=0
        #     r=len(self.stack)-1
        #     while l<r:
        #         m = (l+r) // 2
        #         if self.stack[m]==num:
        #             tempstack = self.stack[:m] + num + self.stack[m:]
        #             continue
        #             r = 0
        #             l = len(self.stack)-1
        #         if self.stack[m]>num:
        #             if self.stack[m-1]<num:
        #                 tempstack = self.stack[:m] + num + self.stack[m:]
        #                 self.stack = tempstack
        #                 r = 0
        #                 l = len(self.stack)-1
        #             else:
        #                 r = m-1
        #         else: #stack[m] < num
        #             if self.stack[m+1] and self.stack[m+1]<num:
        #                 l = m + 1
        #             else:
        #                 tempstack = self.stack[:m] + num + self.stack[m:]
        #                 self.stack = tempstack
        #                 r = 0
        #                 l = len(self.stack)-1
        # print(' addNum() : ', self.stack, 'adding: ', num)
        # if not self.stack:
        #     self.stack.append(num)
        # elif len(self.stack) == 1:
        #     if self.stack[0]>num:
        #         temp = [num, self.stack[0]]
        #         self.stack = temp
        #     else:
        #         self.stack.append(num)
        # else:
        #     for i in range(1, len(self.stack)):
        #         print(i,')  ', self.stack[i] , num)
        #         if num<self.stack[i]:
        #             # print(' num < self.stack[i]')
        #             tempstack = self.stack[:i] + [num] + self.stack[i:]
        #             return
        #     self.stack.append(num)
        # print(' finishing addNum() :', self.stack)

    def findMedian(self) -> float:
        # print(' findMedian() : ', self.stack)
        if len(self.stack) % 2 == 0:
            v1 = self.stack[len(self.stack)//2]
            v2 = self.stack[ (len(self.stack)//2) -1 ]
            return (v1+v2)/2
        else:
            val = self.stack[ len(self.stack)//2 ]
            return val


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()