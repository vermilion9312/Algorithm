n = int(input())

arr = list(map(int, input().split()))

m = max(arr)

arr2 = []

for i in range(len(arr)):
    arr2.append(arr[i] / m * 100)

print(sum(arr2) / len(arr))