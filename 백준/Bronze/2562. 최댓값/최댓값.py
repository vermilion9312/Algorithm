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