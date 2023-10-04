testCase = int(input())

for _ in range(testCase):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if i == 0:
            if a[i] <= 1:
                b = a[i] + 1
            else:
                b = 1
            prvB = b
        else:
            b = prvB + 1
            if b == a[i]:
                b += 1
            prvB = b
    
    print(b)