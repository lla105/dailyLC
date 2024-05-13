class MyStack:

    def __init__(self):
        self.q = deque()
        print(self.q)

    def push(self, x: int) -> None:
        # print('push') 
        self.q.append(x)       

    def pop(self) -> int:
        print(self.q)
        return self.q.pop()
        return 99

    def top(self) -> int:
        # print("top: ", self.q)
        # print("top: ", self.q[-1])
        # print("top: ", self.q[0])
        if self.q[-1]:
            return self.q[-1]

        

    def empty(self) -> bool:
        if len(self.q)==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()