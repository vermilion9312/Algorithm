# https://www.acmicpc.net/problem/10989

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

l = 0
r = len(arr) - 1


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1

    j = l
    while j <= r - 1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return (i + 1)


def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)

        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)


result = quickSort(arr, l, r)
print(result)
