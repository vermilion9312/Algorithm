# https://www.acmicpc.net/problem/3578

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
holes =   [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]

h = int(input())
num = ''

if h % 2 == 0:
    num += '8' * h / 2
else:
    num += '4'
    num += '8' * ((h - 1) // 2)

print(int(num))

'''
1. 처음에는 다양한 숫자의 조합을 생각함
2. 4가 구멍 가진 숫자 중에 제일 작으니깐
   맨 앞에 와야하함
3. 8이 구멍이 두 개니깐 자릿 수를 줄일 수 있음
4. 4와 8만 있으면 됨
5. 구멍 수가 짝수이면 8만 들어가면 되고
6. 홀수이면 4 앞에 들어가고 나머지 8
'''