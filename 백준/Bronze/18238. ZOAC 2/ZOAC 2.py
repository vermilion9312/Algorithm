strAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
intRefDistance = len(strAlphabet) // 2

strInput = input()
intPrvIdx = 0
intCount = 0

for i in range(len(strInput)):
    
    strLetter = strInput[i]
    intCntIdx = strAlphabet.find(strLetter)
    intIdxDiff = abs(intCntIdx - intPrvIdx)
    
    if intIdxDiff <= intRefDistance:
        intCount += intIdxDiff
    else:
        intCount += (len(strAlphabet) - intIdxDiff)

    intPrvIdx = intCntIdx

print(intCount)