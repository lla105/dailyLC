class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        somearray = [0] * n
        somearray[0] = 1
        somearray[1] = 2

        for i in range(2, n):
            somearray[i] = (somearray[i-1]) + (somearray[i-2])
        return somearray[-1]
