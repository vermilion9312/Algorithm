# https://www.acmicpc.net/problem/11720

print("230417-1-1100")

n = int(input())
string = input()

sum = 0
for i in range(n):
    sum += int(string[i])

print(sum)