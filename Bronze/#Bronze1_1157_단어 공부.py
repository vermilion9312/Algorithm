# https://www.acmicpc.net/problem/1157

string = input().upper()

setString = ""

for i in range(len(string)):
    isDuplicate = False
    for j in range(len(string)):

