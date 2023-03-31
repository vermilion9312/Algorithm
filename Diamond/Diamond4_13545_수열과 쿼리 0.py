# https://www.acmicpc.net/problem/13545

n = int(input())
print(n)

arr = list(map(int, input().split()))
print(arr)

m = int(input())

for _ in range(m):
    i, j = map(int, input().split())
    print(i, j)
