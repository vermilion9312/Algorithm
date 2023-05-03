# https://www.acmicpc.net/problem/5585

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

'''
1000 - 380 = 620
500
100
10
10

1000 - 1 = 999
500 * 1
100 * 4
50 * 1
10 * 4
5 * 1
1 * 4
'''