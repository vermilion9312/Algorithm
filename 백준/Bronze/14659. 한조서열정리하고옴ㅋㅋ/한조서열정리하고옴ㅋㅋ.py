# 1차적으로 풀었던 것
# mountainCount = int(input())
# mountain = list(map(int, input().split()))

# killCountList = []
# for i in range(mountainCount):
#     killCount = 0
#     for j in range(mountainCount):
#         if i < j and mountain[i] > mountain[j]:
#             killCount += 1
#             killCountList.append(killCount)
#         if mountain[i] < mountain[j]:
#             break

# print(killCountList)
# print(max(killCountList))

mountainCount = int(input())
mountainList = list(map(int, input().split()))

lastKillCount = 0
highestMountain = 0
killCount = 0

for mountain in mountainList:
    if mountain > highestMountain:
        highestMountain = mountain

        lastKillCount = 0
    else:
        lastKillCount += 1

    killCount = max(lastKillCount, killCount)

print(killCount)