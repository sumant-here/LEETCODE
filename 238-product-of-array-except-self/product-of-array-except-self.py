class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n  = len(nums)
        ans = [1] * n 
        prf = 1
        for i in range(n):
            ans[i] = prf
            prf *= nums[i]
        suff = 1
        for i in range(n-1,-1,-1):
            ans[i] *= suff
            suff *= nums[i]
        return ans 
        

        