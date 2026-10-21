class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0 
        h = len(height) - 1
        maxi = 0 
        while l < h :
            d = h - l
            k = min(height[h],height[l])
            area = d * k 
            maxi = max(area,maxi)
            if height[l] < height[h] :
                l += 1
            else:
                h -= 1
        return maxi
