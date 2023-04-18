# https://www.acmicpc.net/problem/1330

print("230411-2-2220")

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")