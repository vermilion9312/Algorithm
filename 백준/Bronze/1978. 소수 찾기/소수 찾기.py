n = int(input())

arr = list(map(int, input().split()))

count = 0

for v in arr:
    isPrime = True
    
    if v == 1:
        isPrime = False

    for i in range(2, v):
        if v % i == 0:
            isPrime = False

    if isPrime:
        count += 1

print(count)