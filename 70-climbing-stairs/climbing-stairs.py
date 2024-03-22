class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 ... (n-2) = 1
        # 2 ... (n-1) = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        # n = 5
        somearray = [0] * n
        print(somearray)
        somearray[0] = 1
        somearray[1] = 2

        for i in range(2, n):
            # print(somearray[])
            somearray[i] = (somearray[i-1]) + (somearray[i-2])
            # print(f'[{i}] : {somearray[n-1]} + {somearray[n-2]} = {somearray[i]}')
            # print(somearray[n-1] , "+" , somearray[n-2], "=", somearray[i])
        return somearray[-1]
