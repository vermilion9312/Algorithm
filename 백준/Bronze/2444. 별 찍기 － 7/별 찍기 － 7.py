n = int(input())

length = 2 * n - 1
m = 0
for i in range(length):
    if i < length // 2:
        for j in range(n + i):
            if j < n - 1 - i:
                print(" ", end="")
            else:
                print("*", end="")
    else:
        for k in range(length - i + length // 2):
            if k < m:
                print(" ", end="")
            else:
                print("*", end="")
        m += 1
    print()