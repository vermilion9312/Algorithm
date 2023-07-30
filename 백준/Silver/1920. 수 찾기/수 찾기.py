n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

nArr = sorted(nArr)

def binarySearch(val, arr):
    left = 0
    right = len(arr) - 1
    
    check = False

    while left <= right:
        mid = (left + right) // 2
        if val > arr[mid]:
            left = mid + 1
        elif val < arr[mid]:
            right = mid - 1
        else:
            val = arr[mid]
            check = True
            break

    if check:
        print(1)
    else:
        print(0)

for mVal in mArr:
    binarySearch(mVal, nArr)