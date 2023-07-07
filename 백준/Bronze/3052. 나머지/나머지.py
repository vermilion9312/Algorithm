arr = []

while True:
    try:
        arr.append(int(input()) % 42)
    except:
        break

setArr = set(arr)
print(len(setArr))