# https://www.acmicpc.net/problem/2485

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

dArr = []
for i in range(len(arr) - 1):
    d = arr[i + 1] - arr[i]
    dArr.append(d)

print(dArr)

dMin = min(dArr)

print(dMin)

arr2 = []
v = arr[0]
while v <= arr[-1]:
    arr2.append(v)
    v += dMin
print(arr2)
setArr = set(arr)
setArr2 = set(arr2)

print(len(setArr2 - setArr))