class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        temp = []
        for i in range(m):
            for j in range(n):
                if j==0:
                    temp.append(1)
                elif i==0:
                    temp.append(1)
                else:
                    temp.append(0)
            dp.append(temp)
            temp = []

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for each in dp:
            print(each)
        return dp[-1][-1]