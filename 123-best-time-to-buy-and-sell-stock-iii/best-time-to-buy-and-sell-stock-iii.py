class Solution:
    # def solve(self,index,buy,limit,prices):
    #     if index == len(prices):
    #         return 0 
    #     if limit == 0 :
    #         return 0 
    #     if buy == 1:
    #         buy_p = -prices[index] + self.solve(index+1,0,limit,prices)
    #         not_buy = 0  + self.solve(index+1,1,limit,prices)
    #         profit=max(buy_p,not_buy)
    #     else:
    #         sell = prices[index] + self.solve(index+1,1,limit-1,prices)
    #         not_sell = 0 + self.solve(index+1,0,limit,prices)
    #         profit = max(sell,not_sell)
    #     return profit 

    # def maxProfit(self, prices: list[int]) -> int:
    #     n = len(prices)
    #     dp = [[[-1 for _ in range(3)]for _ in range(3)] for _ in range(n+1)]
    #     #base DP = n+1 
    #     for buy in range(0,2):
    #         for limit in range(0,3):
    #             dp[n][buy][limit] = 0 # here 
    #     for index in range(0,n+1):
    #         for buy in range(0,2):
    #             dp[index][buy][0] = 0 
    #     for index in range(n-1,-1,-1):
    #         for buy in range(0,2):
    #             for limit in range(1,3): # here we took 1 bcz upar Le chuke hai 
    #                 if buy == 1:
    #                     buy_p = -prices[index] + dp[index+1][0][limit]
    #                     not_buy = 0  + dp[index+1][1][limit]
    #                     profit=max(buy_p,not_buy)
    #                 else:
    #                     sell = prices[index] + dp[index+1][1][limit-1] # 0-1 = -1 here wrng
    #                     not_sell = 0 + dp[index+1][0][limit]
    #                     profit = max(sell,not_sell)
    #                 dp[index][buy][limit] = profit
    #     return dp[0][1][2]
        # return self.solve(0,1,2,prices)
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        ahead = [[-1 for _ in range(3)]for _ in range(2)]
        #base DP = n+1 
        for buy in range(0,2):
            for limit in range(0,3):
                ahead[buy][limit] = 0 # here 
        # for index in range(0,n+1):
        for buy in range(0,2):
            ahead[buy][0] = 0 
        for index in range(n-1,-1,-1):
            curr = [[-1 for _ in range(3)]for _ in range(2)]
            for buy in range(0,2):
                for limit in range(0,3):
                    if limit  == 0 :
                        profit = 0 
                    elif buy == 1:
                        buy_p = -prices[index] + ahead[0][limit]
                        not_buy = 0  + ahead[1][limit]
                        profit=max(buy_p,not_buy)
                    else:
                        sell = prices[index] + ahead[1][limit-1] # 0-1 = -1 here wrng
                        not_sell = 0 + ahead[0][limit]
                        profit = max(sell,not_sell)
                    curr[buy][limit] = profit
            ahead = curr 
        return ahead[1][2]