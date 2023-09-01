mountainCount = int(input())
mountain = list(map(int, input().split()))

countList = []
for i in range(mountainCount):
    killCount = 0
    for j in range(mountainCount):
        if i < j and mountain[i] > mountain[j]:
            killCount += 1
            countList.append(killCount)
        if mountain[i] < mountain[j]:
            break

print(max(countList))