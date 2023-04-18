# https://www.acmicpc.net/problem/10991

n = 5

for i in range(n):
    for j in range(n + i):
        if j < n - 1 - i:
            print(" ", end="")
        else:
            print(j, end="")
    print()