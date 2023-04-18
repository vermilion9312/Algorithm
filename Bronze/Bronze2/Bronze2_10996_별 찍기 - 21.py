# https://www.acmicpc.net/problem/10996

print("230413-4-2036")

n = int(input())

for i in range(2 * n):
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for j in range(n):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
    print()