n = int(input())
numList = list(map(int, input().split()))
v = int(input())

count = 0

for num in numList:
    if v == num:
        count += 1

print(count)