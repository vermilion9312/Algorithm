# https://www.acmicpc.net/problem/11034

while True:
    try:
        position = list(map(int, input().split()))
        distance1 = abs(position[0] - position[1])
        distance2 = abs(position[1] - position[2])
        if distance1 < distance2:
            print(distance2 - 1)
        else:
            print(distance1 - 1)
    except:
        break

'''
1. 서로 간의 거리가 1이면 종료
2. 양쪽 두 마리 중 캥거루 사이로 뛰는 놈은 거리가 짦은 쪽
3. 캥거루 옆에 바로 붙어서 들어가야 더 많이 뛸 수 있음
4. 거리가 먼 쪽의 캥거루는 가만히 있고
   짧은 쪽의 애가 번갈아가면서 채워감
■■□□□□□□□□□□□□□□□□□□□□■
□■■□□□□□□□□□□□□□□□□□□□■
□□■■□□□□□□□□□□□□□□□□□□■
□□□■■□□□□□□□□□□□□□□□□□■
□□□□■■□□□□□□□□□□□□□□□□■
□□□□□■■□□□□□□□□□□□□□□□■
5. 사실상 두 개의 캥거루가 붙어서
   끝에 있는 캥거루한테까지 한 칸씩 올라가는 형국
6. 첫번 째 점프만 누구로 할지 결정하면 나머지는
   그냥 거리계산 
7. 그냥 점프 카운트를 할 필요가 없네
   그냥 거리계산
'''