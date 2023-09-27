import sys

n, m = map(int, input().split())

lecturRoom = [0] * n

for _ in range(m):

    i, start, end = map(int, sys.stdin.readline().split())
    i -= 1

    if lecturRoom[i] <= start:
        lecturRoom[i] = end
        print("YES")
    else:
        print("NO")