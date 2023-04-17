# https://www.acmicpc.net/problem/1157

print("230417-1-1237")

string = input().upper()
arr = list(set(string))
count = [0 for _ in range(len(arr))]

for i in range(len(arr)):
    for j in range(len(string)):
        if arr[i] == string[j]:
            count[i] += 1

maxNum = max(count)
check = 0
for i in range(len(count)):
    if maxNum == count[i]:
        check += 1
        idx = i
if check >= 2:
    print("?")
else:
    print(arr[idx])

# print(string)
# print(arr)
# print(count)