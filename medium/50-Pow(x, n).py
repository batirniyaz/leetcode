class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x ** n
        return ans
    
ans = Solution()
print(ans.myPow(2.00000, 10))
print(ans.myPow(2.10000, 3))
print(ans.myPow(2.00000, -2))