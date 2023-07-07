while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break

    if a > b and a > c:
        if b * b + c * c == a * a:
            print("right")
        else:
            print("wrong")

    if b > a and b > c:
        if a * a + c * c == b * b:
            print("right")
        else:
            print("wrong")

    if c > b and c > a:
        if a * a + b * b == c * c:
            print("right")
        else:
            print("wrong")