import math

gifts = [56,41,27,71,62,57,67,34,8,71,2,12,52,1,64,43,32,42,9,25,73,29,31]
# counter = 0
# for gift in gifts:
#     counter += 1
# print(counter)


def findmax(gifts):
    i = 1
    k = 52
    while i <= k:
        max_gift = max(gifts)
        if max_gift in gifts:
            gifts.remove(max_gift)
            gifts.append(int(math.sqrt(max_gift)))
        max_gift = 0
        i += 1
    ans = sum(gifts)
    return ans

print(findmax(gifts))
    
        
    

# print(findmax(gifts))