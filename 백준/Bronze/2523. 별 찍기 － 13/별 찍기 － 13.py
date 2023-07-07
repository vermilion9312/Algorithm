n = int(input())
h = 2 * n

for i in range(1, h):
    w = n - abs(i - n)
    for j in range(w):
        print("*", end="")
    print()