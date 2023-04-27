# https://www.acmicpc.net/problem/2740

n, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

m, k = map(int, input().split())

matrix2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(k):
        for l in range(m):
            element = matrix1[i][m] + matrix2[m][j]
            matrix.append(element)

print(matrix1)
print(matrix2)
print(matrix)

