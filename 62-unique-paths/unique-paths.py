class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j ==0:
                    continue
                if i > 0 :
                    up = dp[i-1][j]
                else:
                    up = 0
                if j > 0:
                    left = dp[i][j-1]
                else:
                    left = 0
                dp[i][j] = up + left 
        return dp[m-1][n-1]
        