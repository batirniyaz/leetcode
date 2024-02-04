class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n == 1:
                    return True
                else:
                    return False
            else:
                if n == 1:
                    return False
                else:
                    return True
        i = 0
        while i < len(flowerbed):
            if i != 0 and i != len(flowerbed)-1:
                if flowerbed[i] == 0 and (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                    n -= 1
                    i += 2
                else:
                    i += 1
            elif i == 0:
                if flowerbed[i] == 0 and (flowerbed[i + 1] == 0):
                    n -= 1
                    i += 2
                else:
                    i += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
        if n > 0:
            return False
        else:
            return True


ans = Solution()
print(ans.canPlaceFlowers([0], 1))