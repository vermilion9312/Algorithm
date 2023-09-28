n = int(input())
directionStr = input()

directionCount = [0, 0, 0, 0]

for i in range(n):
    
    if directionStr[i] == 'E':
        directionCount[0] += 1
    if directionStr[i] == 'W':
        directionCount[1] += 1
    if directionStr[i] == 'S':
        directionCount[2] += 1
    if directionStr[i] == 'N':
        directionCount[3] += 1

print(n - max(directionCount))