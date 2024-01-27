import math

gifts = [25, 64, 9, 4, 100]


def findmax(gifts):
    max_gift = 0
    for gift in gifts:
        if gift > max_gift:
            max_gift = gift
    for gift in gifts:
        if gift == max_gift:
            gifts.remove(gift)
    pickGifts(gifts, max_gift)


def pickGifts(gifts, max_gift):
    gifts.append(int(math.sqrt(max_gift)))

    return gifts


def main():
    k = 4
    i = 1
    while i <= k:
        findmax(gifts)
        i += 1
    ans = sum(gifts)
    return ans

print(main())
