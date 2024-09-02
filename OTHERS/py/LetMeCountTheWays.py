from sys import stdin

def count_change(n):
    coins = [1, 5, 10, 25, 50]
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]

for line in stdin:
    amount = int(line.strip())
    ways = count_change(amount)
    if ways == 1:
        print(f"There is only 1 way to produce {amount} cents change.")
    else:
        print(f"There are {ways} ways to produce {amount} cents change.")


