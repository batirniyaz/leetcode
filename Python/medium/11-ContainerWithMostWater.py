class Solution:
    def maxArea(self, height: list[int]) -> int:
        width = len(height) - 1
        capacity = 0
        left, right = 0, width
        while left < right:
            capacity = max((min(height[left], height[right]) * width), capacity)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
            width = right - left
        return capacity

ans = Solution()
print(ans.maxArea([1,8,6,2,5,4,8,3,7]))
            
