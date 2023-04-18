# https://www.acmicpc.net/problem/2442

print("230405-3-1729")

n = int(input())

for i in range(n):
    length = (n - i - 1) + (2 * i - 1) + 2
    for j in range(length):
        if j < n - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()


# 4 + 1  = 5
# 3 + 3 = 6
# 2 + 5 + 7