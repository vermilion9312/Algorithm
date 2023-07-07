changeList = [500, 100, 50, 10, 5, 1]

price = int(input())

change = 1000 - price

count = 0
total = 0
for v in changeList:
    count = change // v
    total += count
    change %= v
print(total)