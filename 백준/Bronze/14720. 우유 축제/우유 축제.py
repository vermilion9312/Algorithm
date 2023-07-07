n = int(input())
store = list(map(int, input().split()))

milkList = [0, 1, 2]

count = 0
idx = 0
# 매장 마다 우유를 마주쳤을 때
for milk in store:
    # 마주친 우유가 딸기 우유라면
    if milk == milkList[idx]:
        # 마신 카운트를 올리고
        count += 1
        # 그 다음 우유를 선택
        idx += 1
        # 근데 index 가 0, 1, 2 반복해야 하니깐 3으로 나눈 나머지 구하기
        idx %= 3
    # else:
    #     continue

print(count)