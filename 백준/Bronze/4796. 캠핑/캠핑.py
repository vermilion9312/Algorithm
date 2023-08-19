caseCount = 1
while True:

    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    q = V // P
    r = V % P
    if L < r:
        r = L
    print("Case %d: %d" %(caseCount, L * q + r))

    caseCount += 1