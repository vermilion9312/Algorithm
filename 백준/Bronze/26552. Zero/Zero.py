n = int(input())

for _ in range(n):

    k = int(input())

    while True:
        k += 1
        if str(k).find('0') == -1:
            print(k)
            break