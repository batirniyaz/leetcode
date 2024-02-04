class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums
        ans.extend(nums)
        return ans
    
ans = Solution()
print(ans.getConcatenation([1,3,2,1]))