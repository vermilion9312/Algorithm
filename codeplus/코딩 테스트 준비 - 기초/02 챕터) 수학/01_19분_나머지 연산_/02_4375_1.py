# https://www.acmicpc.net/problem/4375

# n = 3
# n = 7
# n = 9901

# while True:
#     try:
#         n = int(input())
#     except:
#         break

#     i = 1
#     while True:
#         num = (1 / 9) * (10 ** i) - (1 / 9)
#         num = round(num)
#         if num % n == 0:
#             print(i)
#             break
#         i += 1



# 왜 이거만 맞다고 함?
# while True:
#     try:
#         n = int(input())
#     except:
#         break

#     i = 1
#     num = 0
#     while True:
#         num = 10 * num + 1
#         if num % n == 0:
#             print(i)
#             break
#         i += 1


for i in range(20):
    i += 1
    num = (1 / 9) * (10 ** i) - (1 / 9)
    # num = round(num)
    print(num, i)