n = int(input())

for i in range(n):
    for j in range(n + i):
        if i < n - 1:
            if j < n - 1 - i:
                print(" ", end="")
            elif j > n - 1 - i and j < n - 1 + i:
                print(" ", end="")
            else:
                print("*", end="")
        else:
            print("*", end="")
    print()