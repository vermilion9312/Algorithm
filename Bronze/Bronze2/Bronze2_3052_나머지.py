# https://www.acmicpc.net/problem/3052

print("230418-2-1412")

arr = []

while True:
    try:
        arr.append(int(input()) % 42)
    except:
        break

setArr = set(arr)
print(len(setArr))