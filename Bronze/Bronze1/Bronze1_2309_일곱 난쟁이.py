# https://www.acmicpc.net/problem/2309

n = 9
dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

dwarfs_sum = sum(dwarfs)

for i in range(8):
    for j in range(i + 1, 9):
        if dwarfs_sum - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarfs[k])
            exit()

import sys

n = 9
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(0, n):
    for j in range(i + 1, n):
        total = 0
        for k in range(0, n):
            if i == k or j == k:
                continue
            total += a[k]
        if total == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)

print("오답230418-2-1823")
import sys

total = 0
arr = []
for _ in range(9):
    height = int(input())
    total += height
    arr.append(height)

total -= 100

# 두 명 고르기
arr2 = []
for i in range(len(arr)):
    # 키 한 명 걸 빼고
    total -= arr[i]

    for j in range(len(arr)):
        # 둘은 다르고
        if i != j:
            # 키 한 명 걸 빼고
            total -= arr[j]
        
            if total == 0:
                arr2.append(arr[i])
                arr2.append(arr[j])
                break
            #원복
            else:
                total += arr[j]
    #원복
    if total == 0:
        break
    else:
        total += arr[i]

# 10명 구하기
arr3 = []
for v in arr:
    if v not in arr2:
        arr3.append(v)

arr3.sort()

for v in arr3:
    print(v)

sys.exit(0)

