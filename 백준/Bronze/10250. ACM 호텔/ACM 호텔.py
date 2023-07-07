t = int(input())

for i in range(t):
    result = ""
    h, w, n = map(int, input().split())

    YY = n % h
    if YY == 0:
        YY = h
        XX = n // h
    else:
        XX = n // h + 1

    result += str(YY)
    if XX < 10:
        result += "0"
    result += str(XX)

    print(int(result))