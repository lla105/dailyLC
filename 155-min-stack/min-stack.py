class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack)==0 or self.minstack[-1]>=val:
            self.minstack.append(val)
        # eg stack=[1,2,3] , minstack=[1]
        # eg stack=[] , minstack=[]
        # eg stack=[3,2,1] , minstack=[3,2,1]

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp==self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()