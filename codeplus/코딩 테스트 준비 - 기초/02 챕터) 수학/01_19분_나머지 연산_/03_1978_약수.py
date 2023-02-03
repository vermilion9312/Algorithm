# https://www.acmicpc.net/problem/1978

# n = int(input())
n = 4
# list = list(map(int, input().split()))
list = [1, 3, 5, 7]

ans = 0
for v in list:
    i = 2
    while i * i <= v:
        if v % i != 0:
            ans += 1
        i += 1
print(ans)