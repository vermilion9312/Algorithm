# https://www.acmicpc.net/problem/10952

print("===[230328-2-2045]===")
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)