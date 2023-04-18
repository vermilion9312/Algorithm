# https://www.acmicpc.net/problem/1037

print("===[2023-02-16 (목)]===")

n = int(input())
numList = list(map(int, input().split()))
print(max(numList) * min(numList))