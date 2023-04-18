# https://www.acmicpc.net/problem/10995

print("230413-4-1737")

n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(2 * n - 1):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for j in range(2 * n):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
    print()