# https://www.acmicpc.net/problem/2864

print("230505-5-1700")

a, b = map(int, input().split())

a = int(str(a).replace("5", "6"))
b = int(str(b).replace("5", "6"))

max = a + b

a = int(str(a).replace("6", "5"))
b = int(str(b).replace("6", "5"))

min = a + b

print(min, max)