m, h = map(int, input().split())
n = int(input())

total = 0

for _ in range(n):

    c, b = map(int, input().split())
    if m * c > h * b:
        total += m * c
    else:
        total += h * b
    
print(total)