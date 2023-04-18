# https://www.acmicpc.net/problem/2231

n = input()

num = int(n)

for v in n:
    num -= int(v)

print(num)