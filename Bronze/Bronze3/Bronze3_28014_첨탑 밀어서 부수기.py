# https://www.acmicpc.net/problem/28014

print("230507-7-1227")

n = int(input())
arr = list(map(int, input().split()))

count = 1
for i in range(n - 1):
    if arr[i] <= arr[i + 1]:
        count += 1

print(count)
