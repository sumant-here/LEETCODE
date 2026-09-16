class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n= len(nums)
        target = sum(nums)
        if target % 2 == 1:
            return False
        k = target //2
        prev =[False for _ in range(k+1)]
        prev [0] = True
        if nums[0] <= k :
            prev[nums[0]] = True
        for index in range(1,n):
            curr = [False for _ in range(k+1)]
            for target in range(0,k+1):
                if nums[index] > target:
                    pick = False
                else:
                    pick = prev[target-nums[index]]
                not_pick = prev[target]
                curr[target] = pick or not_pick
            prev = curr
        if prev[k] == True:
            return True
        return False 

