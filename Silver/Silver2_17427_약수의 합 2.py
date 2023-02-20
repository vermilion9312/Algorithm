# https://www.acmicpc.net/problem/17427
# 시간초과
n = int(input())

g = 0
for i in range(n):
    i += 1
    f = 0
    for j in range(i):
        j += 1 
        if i % j == 0:
            f += j
    g += f
print(g)
