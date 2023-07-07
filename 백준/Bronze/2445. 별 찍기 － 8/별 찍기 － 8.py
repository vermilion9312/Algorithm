n = int(input())

h = 2 * n - 1
w = 2 * n

k = 0
for i in range(h):
    if i < h // 2:
        for j in range(w):
            if j >= 1 + i and j <= h - 1 - i:
                print(" ", end="")
            else:
                print("*", end="")
    elif i > h // 2:
        for j in range(w):
            if j >= w // 2 - 1 - k and j <= w // 2 + k:
                print(" ", end="")
            else:
                print("*", end="")
        k += 1
    else:
        for j in range(w):
            print("*", end="")
    print()