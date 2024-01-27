import math


class Solution:
    def pickGifts(self, gifts: [int], k: int) -> int:
        i = 1
        while i <= k:
            max_gift = max(gifts)
            if max_gift in gifts:
                gifts.remove(max_gift)
                gifts.append(int(math.sqrt(max_gift)))
            max_gift = 0
            i += 1
        ans = sum(gifts)
        return ans
    
ans = Solution()
print(ans.pickGifts([25, 64, 9, 100, 4], 4))
