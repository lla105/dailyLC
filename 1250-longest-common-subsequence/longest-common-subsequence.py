class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = text1
        t2 = text2
        if not t1 or not t2:
            return 0
        dp = []
        for i in range(len(t1)):
            temp = [-1] * len(t2)
            # for j in range(len(t2)):
            dp.append(temp)
        # for i in range(len(dp)):
        #     print( dp[i] )

        def LCS(i,j):
            if i==len(t1) or j==len(t2) :
                return 0
            if dp[i][j] != -1 :
                return dp[i][j]
            if t1[i] == t2[j] :
                middle = LCS(i+1, j+1)
                if dp[i][j] == -1:
                    dp[i][j] = middle + 1
                return middle + 1
            else:
                left = LCS(i+1, j)
                right = LCS(i, j+1)
                longest = max(left, right)
                if dp[i][j] == -1 :
                    dp[i][j] = longest
                return longest
        return LCS(0,0)
