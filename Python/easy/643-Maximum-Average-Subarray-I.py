class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0
        ans = sum(nums[0:k])
        while i + k <= len(nums):
            window = sum(nums[i:i + k])
            if window > ans:
                ans = window
            i += 1
        return float(ans) / k

ans = Solution()
print(ans.findMaxAverage([0,1,1,3,3], 4))
print(ans.findMaxAverage([1,12,-5,-6,50,3], 4))
print(ans.findMaxAverage([5], 1))


