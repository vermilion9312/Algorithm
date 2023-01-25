# https://www.acmicpc.net/problem/10162

array = [300, 60, 10]

n = 100
count = 0
for v in array:
    count += n // v
    n %= v
    print(count, end = " ")
