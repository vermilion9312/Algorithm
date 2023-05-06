# https://www.acmicpc.net/problem/11000

n = int(input())

count = 0
classTimeList = []
for _ in range(n):
    classTime = list(map(int, input().split()))
    classTimeList.append(classTime)

for classTime in classTimeList:
