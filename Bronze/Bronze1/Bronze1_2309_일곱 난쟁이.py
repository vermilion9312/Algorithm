# https://www.acmicpc.net/problem/2309

n = 9
dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

dwarfs_sum = sum(dwarfs)

for i in range(8):
    for j in range(i + 1, 9):
        if dwarfs_sum - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarfs[k])
            exit()

// 위의 코드 좀 설명해줘
// 1. 9명의 난쟁이 키를 입력받아 dwarfs 리스트에 저장
// 2. 9명의 난쟁이 키의 합을 구함
// 3. 9명의 난쟁이 키를 2개씩 뽑아서 합이 100이 되는지 확인
// 4. 100이 되면 9명의 난쟁이 키를 출력하고 종료




# import sys

# n = 9
# a = [int(input()) for _ in range(n)]
# a.sort()
# for i in range(0, n):
#     for j in range(i + 1, n):
#         total = 0
#         for k in range(0, n):
#             if i == k or j == k:
#                 continue
#             total += a[k]
#         if total == 100:
#             for k in range(0, n):
#                 if i == k or j == k:
#                     continue
#                 print(a[k])
#             sys.exit(0)


# print("오답230418-2-1823")
# total = 0
# arr = []
# while True:
#     try:
#         height = int(input())
#         total += height
#         arr.append(height)
#     except:
#         break

# total -= 100
# arr2 = []

# for i in range(len(arr)):
#     total -= arr[i]

#     for j in range(len(arr)):
#         if i != j:
#             total -= arr[j]
#             if total == 0:
#                 arr2.append(arr[i])
#                 arr2.append(arr[j])
#                 break
#             else:
#                 total += arr[j]

#     if total == 0:
#         break
#     else:
#         total += arr[i]

# arr3 = []

# for v in arr:
#     if v not in arr2:
#         arr3.append(v)

# arr3.sort()

# for v in arr3:
#     print(v)
