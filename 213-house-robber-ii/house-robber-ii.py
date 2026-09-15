class Solution:

    def solve(self, nums):
        n = len(nums)

        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):

            if i > 1:
                p = nums[i] + dp[i-2]
            else:
                p = nums[i]

            np = dp[i-1]

            dp[i] = max(p, np)

        return dp[n-1]

    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        an1 = self.solve(nums[0:n-1])
        an2 = self.solve(nums[1:n])

        return max(an1, an2)