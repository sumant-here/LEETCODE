class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m= len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        dp[0][0] = grid [0][0]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0 :
                    continue
                if i == 0 :
                    up = float("inf")
                else :
                    up = dp[i-1][j]
                if j == 0 :
                    left = float("inf")
                else:
                    left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up,left)
        return dp[m-1][n-1]