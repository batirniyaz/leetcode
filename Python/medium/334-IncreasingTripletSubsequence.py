import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min = float('inf')
        mid = float('inf')
        for num in nums:
            if num > mid:
                return True
            if num < min:
                min = num
            elif num > min and num < mid:
                mid = num
        return False

ans = Solution()
print(ans.increasingTriplet([1,5,0,4,1,3]))