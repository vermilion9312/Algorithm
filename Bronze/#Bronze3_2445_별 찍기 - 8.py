# https://www.acmicpc.net/problem/2445

n = 5

length = 2 * n - 1

for i in range(length):
    for j in range(2 * n):
        print("*", end=" ")
    print()