# https://www.acmicpc.net/problem/11021

print("===[230328-2-2124]===")
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print("Case #", end="")
    print(i + 1, end="")
    print(":", a + b)