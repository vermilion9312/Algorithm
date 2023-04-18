# https://www.acmicpc.net/problem/2675

print("230418-2-1343")

t = int(input())

for i in range(t):
    r, s = map(str, input().split())

    string = ""

    for i in range(len(s)):
        for j in range(int(r)):
            string += s[i]

    print(string)