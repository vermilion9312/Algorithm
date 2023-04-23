# https://www.acmicpc.net/problem/10992

n = 4

for i in range(n):
    for j in range(n - 1 - i):
        if j < n - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()