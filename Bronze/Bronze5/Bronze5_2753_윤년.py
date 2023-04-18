# https://www.acmicpc.net/problem/2753

print("230417-1-1203")

y = int(input())

if y % 4 == 0:
    if y % 100 != 0 or y % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)