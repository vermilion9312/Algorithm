# https://www.acmicpc.net/problem/2522

print("230413-4-1625")

n = int(input())

h = 2 * n - 1
w = n

k = 0
for i in range(h):
    if i < h // 2:
        for j in range(w):
            if j < w - 1 - i:
                print(" ", end="")
            else:
                print("*", end="")
    elif i > h // 2:
        for j in range(w):
            if j < k + 1: 
                print(" ", end="")
            else:
                print("*", end="")
        k += 1
    else:
        for j in range(w):
            print("*", end="")
    print()