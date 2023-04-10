# https://www.acmicpc.net/problem/2444
import math
n = 5
length = 2 * n - 1
for i in range(length):
    if i < length // 2:
        for j in range(n + i):
            if j < i:
                print("#", end="")
            else:
                print("*", end="")
    else:
        for j in range(length):
            print()

'''
5
6
7
8

'''