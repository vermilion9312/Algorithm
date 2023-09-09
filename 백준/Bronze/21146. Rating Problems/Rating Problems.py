n, k = map(int, input().split())

total = sum([int(input()) for _ in range(k)])

minAvg = (total + (n - k) * (-3)) / n
maxAvg = (total + (n - k) * 3) / n

print(minAvg, maxAvg)