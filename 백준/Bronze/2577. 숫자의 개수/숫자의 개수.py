num = 1
numList = "0123456789"
countList = [0 for _ in range(len(numList))]

while True:
    try:
        num *= int(input())
    except:
        break

strNum = str(num)

for i in range(len(numList)):
    for j in range(len(strNum)):
        if numList[i] == strNum[j]:
            countList[i] += 1

for i in range(len(countList)):
    print(countList[i])