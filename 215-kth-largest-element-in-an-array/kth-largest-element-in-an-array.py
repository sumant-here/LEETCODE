import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(ans,nums[i])
        for i in range(k,n):
            if nums[i]> ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])
        return ans[0]

        # TC - O(k log k) k for k and log k for heapq
        # TC - O(n-k) x log(k) bcz . in heapq it will  be on constant 