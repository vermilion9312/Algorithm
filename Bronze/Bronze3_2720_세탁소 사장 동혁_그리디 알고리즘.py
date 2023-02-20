# https://www.acmicpc.net/problem/2720

print('===[2023-01-25 (수)]===')

charge = [25, 10, 5, 1]

T = int(input())
for _ in range(T):
    C = int(input())
    for cv in charge:
        count = C // cv
        C %= cv
        print(int(count), end = " ")