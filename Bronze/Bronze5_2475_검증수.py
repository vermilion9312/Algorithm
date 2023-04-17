# https://www.acmicpc.net/problem/2475

print("230417-1-1136")

arr = list(map(int, input().split()))

arr2 = []

for i in range(len(arr)):
    arr2.append(arr[i] * arr[i])

print(sum(arr2) % 10)