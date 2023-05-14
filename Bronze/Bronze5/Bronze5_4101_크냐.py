# https://www.acmicpc.net/problem/4101

print("230514-7-2057")

while True:
    a, b = map(int, input().split())
    if a > b:
        print("Yes")
    else:
        if a == 0 and b == 0:
            break
        print("No")

