neededStampCount, pointCardCount = map(int, input().split())

neededPointCardCount = pointCardCount - 1
notEnoughStampCountList = []
minExpense = 0

for _ in range(pointCardCount):

    winningStampCount = list(map(int, input().split()))[0]

    if winningStampCount >= neededStampCount:
        neededPointCardCount -= 1
    else:
        notEnoughStampCountList.append(winningStampCount)

notEnoughStampCountList = list(reversed(sorted(notEnoughStampCountList)))

for i in range(neededPointCardCount):
    minExpense += (neededStampCount - notEnoughStampCountList[i])

print(minExpense)