# https://www.acmicpc.net/problem/13545

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    sum = 0
    count = 0

    idx = i
    while idx <= j:
        sum += arr[idx]
        count += 1
        idx += 1

    if sum == 0:
        print(count)
    else:
        pass
