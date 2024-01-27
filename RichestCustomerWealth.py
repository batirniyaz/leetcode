def maximumWealth():
    accounts = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    max_wealth = 0
    for i in accounts:
        wealth = sum(i)
        if max_wealth < wealth:
            max_wealth = wealth 
    return max_wealth

print(maximumWealth())


print()
