# https://www.acmicpc.net/problem/2884

print("230405-3-1707")

h, m = map(int, input().split())

if h == 0:
    h = 24

time = 60 * h + m
time -= 45

h = time // 60
m = time % 60

if h == 24:
    h = 0

print(h, m)