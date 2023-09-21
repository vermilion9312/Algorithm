n = int(input())

aSite = list(map(int, input().split()))
bSite = list(map(int, input().split()))

moveCount = 0

for i in range(n):
    if aSite[i] > bSite[i]:
        moveCount += (aSite[i] - bSite[i])

print(moveCount)