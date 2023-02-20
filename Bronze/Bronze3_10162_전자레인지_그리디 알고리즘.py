# https://www.acmicpc.net/problem/10162


print('===[2023-01-25 (수)]===')

button = [300, 60, 10]

T = int(input())

count = 0

if T % 10 == 0:
    for v in button:
        count = T // v
        T %= v
        print(count, end = " ")
else:
    print(-1)