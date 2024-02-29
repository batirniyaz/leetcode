class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        if len(word1) < len(word2):
            max_word = word2
            min_word = word1
        else:
            max_word = word1
            min_word = word2
        if len(word1) == len(word2):
            for i in range(len(max_word)):
                ans += word1[i]
                ans += word2[i]
        else:
            for i in range(len(max_word)):
                if i <= len(min_word)-1:
                    ans += word1[i]
                    ans += word2[i]
                else:
                    for j in range(i, len(max_word)):
                        ans += max_word[i:]
                        return ans
        return ans

ans = Solution()
print(ans.mergeAlternately("ab", "pqrs"))