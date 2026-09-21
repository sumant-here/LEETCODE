class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(k+1)]for _ in range(3)] for _ in range(n+1)]
        #base DP = n+1 
        # dp = n+1 x2 x3 (0,1,2)
        for buy in range(0,2):
            for limit in range(0,k+1):
                dp[n][buy][limit] = 0 # here 
        for index in range(0,n+1):
            for buy in range(0,2):
                dp[index][buy][0] = 0 
        for index in range(n-1,-1,-1):
            for buy in range(0,2):
                for limit in range(1,k+1): # here we took 1 bcz upar Le chuke hai 
                    if buy == 1:
                        buy_p = -prices[index] + dp[index+1][0][limit]
                        not_buy = 0  + dp[index+1][1][limit]
                        profit=max(buy_p,not_buy)
                    else:
                        sell = prices[index] + dp[index+1][1][limit-1] # 0-1 = -1 here wrng
                        not_sell = 0 + dp[index+1][0][limit]
                        profit = max(sell,not_sell)
                    dp[index][buy][limit] = profit
        return dp[0][1][k]