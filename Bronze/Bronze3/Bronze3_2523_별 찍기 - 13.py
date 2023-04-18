# https://www.acmicpc.net/problem/2523

print("230413-4-1649")

n = int(input())
h = 2 * n

for i in range(1, h):
    w = n - abs(i - n)
    for j in range(w):
        print("*", end="")
    print()

'''
0 0
1 01
2 012
3 01
4 0
'''