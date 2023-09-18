t = int(input())

for _ in range(t):

    lstInput = list(map(str, input().split()))

    for i in range(len(lstInput)):
        lstInput[i] = lstInput[i][::-1]
    
    lstOutput = lstInput
    print(*lstOutput)