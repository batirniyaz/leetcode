class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars:
            return 0

        readPointer, writePointer = 0, 0

        while readPointer < len(chars):
            currentChar = chars[readPointer]
            count = 0

            while readPointer < len(chars) and chars[readPointer] == currentChar:
                readPointer += 1
                count += 1

            chars[writePointer] = currentChar
            writePointer += 1

            if count > 1:
                for digit in str(count):
                    chars[writePointer] = digit
                    writePointer += 1

        return writePointer
    
ans = Solution()
print(ans.compress(["a","a","b","b","c","c","c"]))