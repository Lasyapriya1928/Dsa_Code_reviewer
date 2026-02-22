def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    min_coins = float("inf")
    for coin in coins:
        res = coin_change_recursive(coins, amount - coin)
        if res != float("inf"):
            min_coins = min(min_coins, res + 1)

    return min_coins


print(coin_change_recursive([1,2,5], 5))