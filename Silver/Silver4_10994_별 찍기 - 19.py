# https://www.acmicpc.net/problem/10994

n = 3
for i in range(1, 4 * n - 2):
    if i == 1 or i == 4 * n - 3:
        print("*" * (4 * n - 3))
    else:
        print("*" + " " * (4 * n - 5) + "*")

'''
n = 1
print("*")

n = 2
print("*****")
print("*   *")
print("* * *")
print("*   *")
print("*****")

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * (4 * n - 3))
    else:
        print("*" + " " * (4 * n - 5) + "*")


n = 3
print("*********")
print("*       *")
print("* ***** *")
print("* * * * *")
print("* ***** *")
print("*       *")
print("*********")
'''