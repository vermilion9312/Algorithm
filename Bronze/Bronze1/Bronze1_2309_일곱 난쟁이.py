# https://www.acmicpc.net/problem/2309

print("오답230418-2-1823")

total = 0
arr = []
for _ in range(9):
    height = int(input())
    total += height
    arr.append(height)

total -= 100
restore = total

for i in range(len(arr)):
    for j in range(len(arr)):
         if i != j:
            total -= (arr[i] + arr[j])
            if total == 0:
                idx1 = i
                idx2 = j
                break
            else:
                total = restore
                
del(arr[idx1])
del(arr[idx2])

arr.sort()

for v in arr:
    print(v)






