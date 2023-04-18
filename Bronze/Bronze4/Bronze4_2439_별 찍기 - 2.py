# https://www.acmicpc.net/problem/2439

print("230405-3-1651")
n = int(input())

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print("")

print("안성현")
for i in range(1, n + 1) :
    print(" " * (n - i) + "*" * i) 


'''
01234
01234
01234
01234
01234
'''