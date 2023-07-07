n = int(input())

for i in range(n):
    i += 1
    for j in range(2 * n - i):
        j += 1
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print()