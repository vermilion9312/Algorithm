t = int(input())

for i in range(t):
    string = input()

    count = 0
    total = 0

    for v in string:
        if v == "O":
            count += 1
            total += count
        else:
            count = 0

    print(total)