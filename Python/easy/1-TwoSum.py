class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

ans = Solution()
print(ans.twoSum([3, 2, 3], 6))