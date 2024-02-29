class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        return nums


ans = Solution()
print(ans.moveZeroes([0,1,0,3,12]))
print(ans.moveZeroes([0,0,1]))
print(ans.moveZeroes([0]))