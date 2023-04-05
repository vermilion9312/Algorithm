# https://www.acmicpc.net/problem/2441

print("230405-3-1716")

n = int(input())

for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print("")