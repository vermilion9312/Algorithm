n = int(input())

for i in range(n):
    length = (n - i - 1) + (2 * i - 1) + 2
    for j in range(length):
        if j < n - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()