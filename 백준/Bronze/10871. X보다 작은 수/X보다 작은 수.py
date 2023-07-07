n, x = map(int, input().split())

arr = list(map(int, input().split()))

string = ""

for i in range(n):
    if arr[i] < x:
        string += str(arr[i])
        if i < n - 1:
            string += " "
print(string)