intCandyBundleNum = int(input())
listCandyBundle = list(map(int, input().split()))

def chooseMinCandyBundle():
    
    intMinCandyNum = 1000

    for intCandyNum in listCandyBundle:
        if intCandyNum % 2 != 0 and intCandyNum < intMinCandyNum:
            intMinCandyNum = intCandyNum
    
    return intMinCandyNum

intCandyTotalNum = sum(listCandyBundle)

if intCandyTotalNum % 2 != 0:
    intMinCandyNum = chooseMinCandyBundle()
    intCandyTotalNum -= intMinCandyNum

print(intCandyTotalNum)