m, n = map(int, input().split())

arr = [v + 1 for v in range(m)]

def sorting(i, j):
    i -= 1
    j -= 1
    if abs(i - j) >= 0 and abs(i - j) <= 1:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        length = abs(i - j) // 2
        k = 0
        while k <= length:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            k += 1
    return arr

for _ in range(n):
    i, j = map(int, input().split())
    arr = sorting(i, j)

for v in arr:
    print(v, end=" ")