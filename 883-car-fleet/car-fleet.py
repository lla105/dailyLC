class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for i in range(len(speed)):
            stack.append( (position[i], speed[i]) )
        stack = sorted(stack, key=lambda x:x[0] )

        stack2 = []
        for i in range(len(stack)-1, -1, -1):
            timeleft = (target - stack[i][0]) / stack[i][1]
            # print(i,timeleft)
            if not stack2 or stack2[-1] < timeleft:
                stack2.append( timeleft )
        return len(stack2)