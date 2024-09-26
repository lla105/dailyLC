class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.arr)):
            a = self.arr[i][0]
            b = self.arr[i][1]
            c = start
            d = end
            cond1 = (c<b and a<=c)
            cond2 = (a<d and d<=b)
            cond3 = (c<=a and a<b and b<=d)
            if cond1 or cond2 or cond3 :
                return False
        self.arr.append( (start, end) )
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)