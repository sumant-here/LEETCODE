class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m= len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in  range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0
                    continue
                if i == 0 :
                    up  = 0 
                else: 
                    up = dp[i-1][j]
                if j == 0 :
                    left = 0
                else:
                    left = dp[i][j-1]
                dp[i][j] = up  + left 
        return dp[m-1][n-1]
        