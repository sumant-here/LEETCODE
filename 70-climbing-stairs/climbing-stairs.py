class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [-1] * (n+ 1)
        # def dfs(i):
        #     if i == 1:
        #         return 1
        #     if i == 2 :
        #         return 2 
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = dfs(i-1) + dfs(i -2)
        #     return dp[i]
        # return dfs(n)
        # if n == 1:
        #     return 1
        # dp = [0] * (n+ 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        if n == 1:
            return 1
        prev2 = 1
        prev1 = 2
        for i in range(3, n + 1):
            curr =  prev2 + prev1
            prev2 = prev1
            prev1 = curr
        return prev1 