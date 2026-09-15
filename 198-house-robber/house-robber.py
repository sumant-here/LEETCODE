class Solution: 
    def rob(self, nums: List[int]) -> int: 
        n = len(nums) 
        dp = [-1] * n 
 
        def solve(i): 
 
            if i == 0: 
                return nums[i] 
 
            if i < 0: 
                return 0 
            
            if dp[i] != -1: 
                return dp[i] 
 
            p = nums[i] + solve(i - 2) 
            np = solve(i - 1) 
 
            dp[i] = max(p, np)

            return dp[i]   # <-- missing
 
        return solve(n - 1)