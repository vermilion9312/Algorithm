# https://www.acmicpc.net/problem/1920

import math

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targetArr = list(map(int, input().split()))


arr = sorted(arr)

for target in targetArr:
    left = arr[0]
    right = arr[-1] + 1

    check = True
    while True:
        mid = math.floor((left + right) / 2)
        if target > mid:
            left = mid
        elif target < mid:
            right = mid
        else:
            print("1")
            check = False
            break

        if left == right or left + 1 == right:
            print("0")
            break