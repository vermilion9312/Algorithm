# https://www.acmicpc.net/problem/10430

print('===[2023-01-29 (일)]===')

A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
