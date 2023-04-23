# https://www.acmicpc.net/problem/10991

print("230423-7-1720")

n = int(input())

for i in range(n):
    for j in range(n + i):
        if j < (n - 1) - i:
            print(" ", end="")
        else:
            if n % 2 == 0:
                if i % 2 == 0:
                    if j % 2 != 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    if j % 2 != 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
    print()