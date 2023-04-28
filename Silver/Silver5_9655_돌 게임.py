# https://www.acmicpc.net/problem/9655

# n = 5

'''
상근(SK) 창영(CY)

상근
n -= 1 // n == 4

창영
n -= 1 // n == 3

상근
n -= 1 // n == 2

창영
n -= 1 // n == 1

상근
n -= 1 // n == 0
================
상근
n -= 3 // n



===================
1 + 1 = 2 
1 + 3 = 4
3 + 1 = 4
3 + 3 = 6
2 | 2 4 6
    1 2 3
    12
'''

# n = int(input())

# if n >= 6:
#     if n % 6 == 1:
#         print("CY")
#     elif n % 6 == 2:
#         print("")
#     elif n % 6 == 3:
#         print("")
#     elif n % 6 == 4:
#         print("")
#     elif n % 6 == 5:
#         print("")
#     elif n % 6 == 0:
#         print("")
        
# elif n >= 4 and n < 5:
#     if n % 4 == 1:
#         print("CY")
#     elif n % 4 == 2:
#         print("SK")
#     elif n % 4 == 3:
#         print("SK")
#     elif n % 4 == 0:
#         print("SK")
# else:
#     if n % 2 == 1:
#         print("CY")
#     elif n % 2 == 0:
#         print("SK")

'''
n % 6 == 1 상근승
n % 6 == 2 창영승
n % 6 == 3 상근승
n % 6 == 4 상근승
n % 6 == 5 상근승
n % 6 == 0 창영승

n % 4 == 1 상근승
n % 4 == 2 창영승
n % 4 == 3 상근승
n % 4 == 0 창영승

n % 2 == 1 상근승 
n % 2 == 0 창영승
'''
print("230428-5-1615")

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")
