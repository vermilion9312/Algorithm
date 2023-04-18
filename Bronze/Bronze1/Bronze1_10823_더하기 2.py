# https://www.acmicpc.net/problem/10823

print("230411-1-1745")

string = ""

while True:
    try:
        string += input()
    except:
        break

print(sum(map(int, string.split(","))))

    