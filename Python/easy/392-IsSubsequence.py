class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    
ans = Solution()
print(ans.isSubsequence("b", "abc"))
print(ans.isSubsequence("acb", "ahbgdc"))
print(ans.isSubsequence("abc", "ahbgdc"))
print(ans.isSubsequence("", "ahbgdc"))