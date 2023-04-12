# https://www.acmicpc.net/problem/2446

print("230412-3-1620")

n = int(input())

l = 2 * n - 1
k = 0
for i in range(l):
    if i < l // 2:
        for j in range(l):
            if j >= 0 + i and j <= l - 1 - i:
                print("*", end="")
            elif j < 0 + i:
                print(" ", end="")
    elif i > l // 2:
        for j in range(l):
            if j >= l // 2 - 1 - k and j <= l // 2 + 1 + k:
                print("*", end="")
            elif j < l // 2 - 1 - k:
                print(" ", end="")
        k += 1
    else:
        for j in range(l):
            if i == j:
                print("*", end="")
            elif j < i:
                print(" ", end="")
    print()