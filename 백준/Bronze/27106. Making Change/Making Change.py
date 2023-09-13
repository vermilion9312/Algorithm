price = int(input())
change = 100 - price

coin = [25, 10, 5, 1]
coinCount = []

for i in range(len(coin)):
    coinCount.append(change // coin[i])
    change %= coin[i]

print(*coinCount)