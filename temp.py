# n = 2

# for i in range(4 * n - 3):
#     for j in range(4 * n - 3):
#         print("*", end="")
#     print()


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print(sum(10))