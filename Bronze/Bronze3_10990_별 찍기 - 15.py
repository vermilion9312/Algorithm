# https://www.acmicpc.net/problem/10990

print("230413-4-1717")

n = int(input())

for i in range(n):
    for j in range(n + i):
        if j < n - 1 - i:
            print(" ", end="")
        elif j > n - 1 - i and j < n - 1 + i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

