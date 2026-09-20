class Solution:
    # def solve(self,index,buy,prices):
    #     if index == len(prices):
    #         return 0 
    #     if  buy == 1:
    #         buy = -prices[index] + self.solve(index+1,0,prices)
    #         not_buy = 0 +self.solve(index+1,1,prices)
    #         profit = max(buy,not_buy)
    #     else:
    #         sell = prices[index] + self.solve(index+1,1,prices)
    #         not_sell = 0 + self.solve(index+1,0,prices)
    #         profit = max(sell,not_sell)
    #     return profit
    # def maxProfit(self, prices: list[int]) -> int:
    #     n = len(prices)
    #     dp = [[-1,-1] for _ in range(n+1)]
    #     dp[n][0] = 0
    #     dp[n][1]   = 0 # start from pocho 
    #     #TC - O(Nx2) for index and buy or sell 
    #     #SC - O(Nx2) qand i remove stack complecity
    #     for index in range(n-1,-1,-1): 
    #         for buy in range(0,2): #01
    #             if buy == 1:
    #                 buy_p = -prices[index] + dp[index+1][0]
    #                 not_buy = 0 + dp[index+1][1]
    #                 profit  = max(buy_p,not_buy)
    #             else:
    #                 sell = prices[index] + dp[index+1][1]
    #                 not_sell = 0 + dp[index+1][0]
    #                 profit = max(sell,not_sell)
    #             dp[index][buy] = profit
    #     return dp[0][1]
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        ahead = [-1,-1]
        ahead = [0,0]
 # start from pocho 
        #TC - O(Nx2) for index and buy or sell 
        #SC - O(Nx2) qand i remove stack complecity
        for index in range(n-1,-1,-1): 
            curr = [-1,-1]
            for buy in range(0,2): #01
                if buy == 1:
                    buy_p = -prices[index] + ahead[0]
                    not_buy = 0 +  ahead[1]
                    profit  = max(buy_p,not_buy)
                else:
                    sell = prices[index] + ahead[1]
                    not_sell = 0 +  ahead[0]
                    profit = max(sell,not_sell)
                curr[buy] = profit
            ahead = curr
        return ahead[1]




        