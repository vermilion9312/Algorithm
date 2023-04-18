# https://www.acmicpc.net/problem/1085

print("230418-2-1529")

x, y, w, h = map(int, input().split())

arr = [abs(x - 0), abs(x - w), abs(y - 0), abs(y - h)]

print(min(arr))