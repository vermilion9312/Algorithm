numList = []

for _ in range(28):
    numList.append(int(input()))

for i in range(1, 31):
    if i not in numList:
        print(i)