# https://www.acmicpc.net/problem/2438

print("230405-3-1602")

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()