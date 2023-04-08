# https://www.acmicpc.net/problem/2444

n = 5
length = 2 * n - 1
for i in range(length):
    i += 1
    if i < length:
        print("#", end="")
    else:
        print()

    # for j in range(2 * n - 1):
    #     j += 1
    #     print(j, end="")
    # print()