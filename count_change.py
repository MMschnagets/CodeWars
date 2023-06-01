def count_change(money, coins):
    ways = [0] * (money + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]


print(count_change(11, [5, 7]))
