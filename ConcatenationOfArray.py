
def getConcatenation():
    nums = [1, 2, 3]
    ans = []
    n = len(nums)
    for i in range(n):
        ans.append(nums[i])
    for i in range(n):
        ans.append(nums[i])
    
    return ans

print(getConcatenation())