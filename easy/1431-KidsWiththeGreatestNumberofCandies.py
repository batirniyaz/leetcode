class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        great_kid = max(candies)
        for candie in candies:
            kid = candie + extraCandies
            if kid >= great_kid:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            

ans = Solution()
print(ans.kidsWithCandies([2,3,5,1,3], 3))