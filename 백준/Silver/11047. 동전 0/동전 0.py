n, k = map(int, input().split())

coinList = []

for _ in range(n):
    coinList.append(int(input()))

coinList = coinList[::-1]

coinCount = 0

for coin in coinList:
    coinCount += k // coin
    k %= coin

    if k == 0:
        break

print(coinCount)