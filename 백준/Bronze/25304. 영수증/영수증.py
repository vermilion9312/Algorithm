total = int(input())
n = int(input())

for _ in range(n):
    price, count = map(int, input().split())
    total -= price * count

if total == 0:
    print("Yes")
else:
    print("No")