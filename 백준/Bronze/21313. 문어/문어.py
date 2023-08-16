intOctopusNum = int(input())

strOctopusSequence = "1 2 " * (intOctopusNum // 2)

if intOctopusNum % 2 == 0:
    print(strOctopusSequence.strip())
else:
    print(strOctopusSequence + "3")