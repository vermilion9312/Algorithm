# https://www.acmicpc.net/problem/2908

print("0230418-2-1355")

a, b = map(str, input().split())

a = int("".join(reversed(a)))
b = int("".join(reversed(b)))

if a > b:
    print(a)
else:
    print(b)