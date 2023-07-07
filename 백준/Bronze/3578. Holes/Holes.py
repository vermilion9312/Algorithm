h = int(input())
num = ''
if h == 0:
    num = '1'
elif h == 1:
    num = '0'
elif h % 2 == 0:
    num += '8' * (h // 2)
else:
    num += '4'
    num += '8' * ((h - 1) // 2)

print(int(num))