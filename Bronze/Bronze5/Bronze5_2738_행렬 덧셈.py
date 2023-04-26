# https://www.acmicpc.net/problem/2738

print("230425-2-1110")

n, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrixSum = []
for i in range(n):
    matrixSum.append([])
    for j in range(m):
        element = matrix1[i][j] + matrix2[i][j]
        matrixSum[i].append(element)

for row in matrixSum:
    for element in row:
        print(element, end=" ")
    print()

