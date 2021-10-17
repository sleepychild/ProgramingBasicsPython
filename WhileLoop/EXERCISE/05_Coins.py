coins: tuple = (2.0, 1.0, .5, .2, .1, .05, .02, .01)

coins_count: int = int()
coin_count: int = int()

remainder: float = float(input())

for coin in coins:
    coin_count, remainder = divmod(round(remainder, 2), coin)
    coins_count += int(coin_count)
    if remainder == 0:
        print(coins_count)
        exit(0)
