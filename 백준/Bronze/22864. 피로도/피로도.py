fatigueList = list(map(int, input().split()))
intA = fatigueList[0]
intB = fatigueList[1]
intC = fatigueList[2]
intM = fatigueList[3]

intFatigue = 0
intWork = 0
for _ in range(24):

    if (intFatigue + intA) <= intM:
        intFatigue += intA
        intWork += intB
    else:
        intFatigue -= intC
        if intFatigue < 0:
            intFatigue = 0
            
print(intWork)