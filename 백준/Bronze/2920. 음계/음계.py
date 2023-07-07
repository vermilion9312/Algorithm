arr = list(map(int, input().split()))

asc = 0
dsc = 0
for i in range(len(arr) - 1):
    if arr[i] + 1 == arr[i + 1]:
        asc += 1
    elif arr[i] - 1 == arr[i + 1]:
        dsc += 1

if asc == len(arr) - 1:
    print("ascending")
elif dsc == len(arr) - 1:
    print("descending")
else:
    print("mixed ")