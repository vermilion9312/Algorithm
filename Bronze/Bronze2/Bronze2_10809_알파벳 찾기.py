# https://www.acmicpc.net/problem/10809

print("230418-2-1454")

string = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = ''

for i in range(len(alphabet)):
    if alphabet[i] in string:
        result += str(string.index(alphabet[i]))
    elif alphabet[i] not in string:
        result += "-1"

    if i != len(alphabet) - 1:
        result += " " 

print(result)