# https://www.acmicpc.net/problem/4375


print('===[2023-02-02 (목)]===')

# n = 3
# n = 7
# n = 9901

# 컴퓨터는 실수 계산을 못 한다
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


# print("===[내풀이: 160ms]===")
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

# print("===[다른사람풀이: 40ms]===")
# while True:
#     try:
#         n = int(input())
#     except:
#         break
#     num = 0
#     i = 1
#     while True:
#         num = num * 10 + 1
#         num %= n # 요거 두 줄로
#         if num == 0: # 1/4 더 빠른 풀이
#             print(i)
#             break
#         i += 1


for i in range(20):
    i += 1
    num = (1 / 9) * (10 ** i) - (1 / 9)
    num = int(num)
    print(num)
