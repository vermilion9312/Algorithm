# https://www.acmicpc.net/problem/2562

print("230417-1-1436")

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

maxNum = max(arr)
print(maxNum)

for i in range(len(arr)):
    if maxNum == arr[i]:
        print(i + 1)
        break