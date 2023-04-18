# https://www.acmicpc.net/problem/2443

print("230407-6-2226")

n = int(input())

for i in range(n):
    i += 1
    for j in range(2 * n - i):
        j += 1
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

'''
123456789
1|2345678|9
12|34567|89
123|456|789
1234|5|6789
'''