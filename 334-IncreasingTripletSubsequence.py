import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min, mid = sys.maxsize, sys.maxsize
        
        for j in nums:
            if j > mid:
                return True
            if j < min:
                min = j
            elif j < mid:
                mid = j
            j += 1
        return False

ans = Solution()
print(ans.increasingTriplet([1,5,0,4,1,3]))
print(ans.increasingTriplet([4,5,2147483647,1,2]))
print(ans.increasingTriplet([20,100,10,12,5,13]))
print(ans.increasingTriplet([0,4,2,1,0,-1,-3]))
print(ans.increasingTriplet([2,1,5,0,4,6]))
print(ans.increasingTriplet([2,4,-2,-3]))