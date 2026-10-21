class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l =  0 
        h = len(numbers) - 1
        while l < h :
            to = numbers[l] + numbers[h]
            if to == target :
                return [l+1 , h+1]
            elif to < target :
                l += 1
            else :
                h -= 1

        